from django.db import models

import uuid

# Create your models here.


class BaseModelClass(models.Model):

    uuid = models.SlugField(unique=True,default=uuid.uuid4)

    active_status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        abstract = True

class Job(BaseModelClass):
    JOB_TYPES = [
        ('full_time', 'Full time'),
        ('part_time', 'Part time'),
        ('internship', 'Internship'),
        ('contract', 'Contract'),
    ]

    title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=100)
    company_website = models.URLField(blank=True)
    company_email = models.EmailField()
    location = models.CharField(max_length=100)
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    yearly_salary = models.IntegerField(blank=True, null=True)
    vacancies = models.IntegerField(default=1)
    job_type = models.CharField(max_length=20, choices=JOB_TYPES, default='full_time')
    description = models.TextField()
    required_skills = models.TextField(help_text="List skills separated by commas.")
    education_experience = models.TextField()
    posted_date = models.DateField(auto_now_add=True)
    application_deadline = models.DateField()


    def __str__(self):
        return self.title