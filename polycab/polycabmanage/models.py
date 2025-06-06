from django.db import models


# Create your models here.

class User(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Project Manager', 'Project Manager'),
        ('Site Engineer', 'Site Engineer'),
        ('Surveyor', 'Surveyor'),
        ('ROW Coordinator', 'ROW Coordinator'),
        ('Quality Inspector', 'Quality Inspector'),
        ('User', 'User'),
        ('Viewer', 'Viewer'),
    ]
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)


    def __str__(self):
        return self.full_name


    
class Task(models.Model):
    STATES_CHOICES = [
        ('Bihar', 'Bihar'), ('Gujarat','Gujarat'),('UP', 'Uttar Pradesh'), ('Haryana','Haryana'),('Delhi', 'Delhi'), ('Himachal Pradesh','Himachal Pradesh'),('AP','Andhra Pradesh'),('Jharkhand','Jharkhand'),('MP','Madhya Pradesh'),('Arunachal Pradesh','Arunachal Pradesh'),('Assam','Assam'),('Chhattisgarh','Chhattisgarh'),('Goa','Goa'),('Rajasthan', 'Rajasthan'),('Sikkim', 'Sikkim'),('Tamil Nadu', 'Tamil Nadu'),('Telangana', 'Telangana'),('Tripura', 'Tripura'),('Uttar Pradesh', 'Uttar Pradesh'),('Uttarakhand', 'Uttarakhand'),('West Bengal', 'West Bengal')
    ]

    MILESTONES_CHOICES = [
        ('Desktop Survey Design','Desktop Survey Design'),
        ('Design / Network-Health-Checkup', 'Design / Network-Health-Checkup'),
        ('HOTO-Existing', 'HOTO-Existing'),
        ('Detailed Design','Detailed Design'),
        ('ROW(Right of Way)','ROW(Right of Way)'),
        ('IFC(Issued for Comnstruction)','IFC(Issued for Comnstruction)'),
        ('IC(Intial Construction)','IC(Intial Construction)'),
        ('As-Built','As-Built'),
        ('HOTO (Final)', 'HOTO (Final)')
    ]
    BLOCK_CHOICES = [
        ('Block A', 'Block A'),
        ('Block B', 'Block B'),
        ('Block C', 'Block C'),
    ]
    
    BUSINESS_AREA_CHOICES = [
        ('Area1', 'Area1'),
        ('Area2', 'Area2'),
        ('Area3', 'Area3'),
    ]
    STATUS_CHOICES=[
        ('completed','Completed'),
        ('inprogress','Inprogress'),
        ('nill','Nill')
    ]
    state = models.CharField(max_length=100, choices=STATES_CHOICES)
    block = models.CharField(max_length=100, choices=BLOCK_CHOICES)
    milestone = models.CharField(max_length=100, choices=MILESTONES_CHOICES)
    business_area = models.CharField(max_length=100, choices=BUSINESS_AREA_CHOICES)
    district = models.CharField(max_length=100)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    subtasks = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status=models.CharField(max_length=100,choices=STATUS_CHOICES)

    def __str__(self):
        return self.name



