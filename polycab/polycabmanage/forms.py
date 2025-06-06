from django import forms
from .models import User,Task
from django.contrib.auth.forms import AuthenticationForm

class AddUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['full_name','email','phone','role']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
        }

class TaskForm(forms.ModelForm):
    assigned_to = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['assigned_to'].label_from_instance = lambda obj: obj.full_name
        self.fields['state'].widget.attrs.update({'class': 'form-control'})
        self.fields['district'].widget.attrs.update({'class': 'form-control'})
        self.fields['business_area'].widget.attrs.update({'class': 'form-control'})
        
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'block': forms.Select(attrs={'class': 'form-control'}),
            'milestone': forms.Select(attrs={'class': 'form-control'}),
            'business_area': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Task Name'}),
            'subtasks': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Subtasks'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


