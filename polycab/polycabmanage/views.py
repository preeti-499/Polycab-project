from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddUserForm, TaskForm
from .models import User, Task
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:
            auth_login(request, user)
            return redirect('admindash')
        else:
            messages.error(request, 'Invalid Admin Credentials.')
            return redirect('login')
    
    return render(request, 'login.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)  # authenticate handles find + verify
        print(user)
        if user is not None:
            auth_login(request, user)  # login creates session automatically
            return redirect('user_dashboard')  # or 'admindash' if user.is_superuser
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password'})
    
    return render(request, 'login.html')


def LogoutView(request):
    return redirect('login')

@login_required
def admin_dashboard(request):
    users = User.objects.all()
    return render(request, 'admin.html',{'users':users})

@login_required
def user_dashboard(request):
    tasks = Task.objects.all()
    return render(request, 'user.html', {'tasks': tasks})

def dashboard(request):
    selected_state = request.GET.get('state', None)
    if selected_state:
        tasks = Task.objects.filter(state=selected_state)
    else:
        tasks = Task.objects.all()

    milestone = ['Desktop Survey Design', 'Network Health Checkup', 'Hoto Existing','Detailed Design','ROW(Right of Way)','IFC(Issued for Comnstruction)','IC(Intial Construction)','As-Built','HOTO (Final)']

    milestone_data = {}

    for m in milestone:
        milestone_tasks = tasks.filter(milestone=m)
        nill_count = milestone_tasks.filter(status='nill').count()
        inprogress_count = milestone_tasks.filter(status='inprogress').count()
        completed_count = milestone_tasks.filter(status='completed').count()

        total_count = nill_count + inprogress_count + completed_count

        if selected_state:
            if total_count > 0:   # Only add if there are tasks
                milestone_data[m] = {
                    'nill': nill_count,
                    'inprogress': inprogress_count,
                    'completed': completed_count,
                }
        else:
            milestone_data[m] = {
                'nill': nill_count,
                'inprogress': inprogress_count,
                'completed': completed_count,
            }

    states = Task.objects.values_list('state', flat=True).distinct()

    return render(request, 'admindash.html', {
        'milestone_data': milestone_data,
        'states': states,
        'selected_state': selected_state,
    })


def add_user(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if form.is_valid():
            if password == confirm_password:
                user = form.save(commit=False)
                user.is_active = True  
                user.save()
                return redirect('admin.html') 
            else:
                form.add_error(None, "Passwords do not match.")

    else:
        form = AddUserForm()

    return render(request, 'adduser.html', {'form': form})



def update_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        form = AddUserForm(request.POST, instance=user)
        if form.is_valid():
            user.save()
        return redirect('admin_dashboard') 
    else:
        form=AddUserForm(instance=user) 
    return render(request, 'update.html', {'form': form})

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('admin_dashboard') 


def task(request):
    tasks = Task.objects.all()
    return render(request,'task.html', {'tasks': tasks})

def addtask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task')
    else:
        form = TaskForm()
    return render(request,'addtask.html', {'form': form})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task')
    else:
        form = TaskForm(instance=task)
    return render(request, 'uptask.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task') 

def user_mytasks(request):
    users = User.objects.all()
    user_tasks = {}
    for user in users:
        tasks = Task.objects.filter(assigned_user=user)
        user_tasks[user] = tasks
    return render(request, 'all_users_tasks.html', {'user_tasks': user_tasks})