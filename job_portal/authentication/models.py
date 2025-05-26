from django.db import models
from django.contrib.auth.models import User

class CustomUser(models.Model):

    ROLE_CHOICES = (
        ('employer','Employer'),
        ('job_seeker','Job Seeker'),
     )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):

        return f"{self.user.username} - {self.role}"
    

class EmployerProfile(models.Model):

    custom_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    website = models.URLField(blank=True)
    industry = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):

        return self.company_name
    
class JobSeekerProfile(models.Model):

    custom_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    resume = models.FileField(upload_to='resume/')
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=100)

    def __str__(self):

        return self.full_name

