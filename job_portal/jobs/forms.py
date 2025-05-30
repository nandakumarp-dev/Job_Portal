from django import forms
from .models import JobPost

class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = [
            'title', 'company_name', 'company_website', 'company_email',
            'location', 'salary_min', 'salary_max', 'yearly_salary',
            'vacancies', 'job_type', 'description', 'required_skills',
            'education_experience', 'application_deadline'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'required_skills': forms.Textarea(attrs={'rows': 3}),
            'education_experience': forms.Textarea(attrs={'rows': 3}),
            'application_deadline': forms.DateInput(attrs={'type': 'date'}),
        }
