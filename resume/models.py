from django.db import models

from employee.models import Employee


class Job(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    responsibility = models.TextField()
    location = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}: {self.role}"


class Resume(models.Model):
    position = models.CharField(max_length=100)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name="resumes")
    summary = models.TextField()
    experience = models.ManyToManyField(Job, related_name="resumes")
    education = models.TextField()
    skills = models.TextField()

    def __str__(self):
        return f"{self.employee.get_full_name()}: {self.position}"
