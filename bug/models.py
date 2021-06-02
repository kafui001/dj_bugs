from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser



# Create your models here.
class BugUser(AbstractUser):
    is_developer       = models.BooleanField(default=False)
    is_project_manager = models.BooleanField(default=True)

 
class UserProfile(models.Model):
    user = models.OneToOneField(BugUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class ProjectManager(models.Model):
    user  = models.OneToOneField(BugUser,on_delete=models.CASCADE)
    admin = models.ForeignKey(UserProfile,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Developer(models.Model):
    user              = models.OneToOneField(BugUser,on_delete=models.CASCADE)
    project_manager   = models.ForeignKey(ProjectManager, on_delete=models.SET_NULL, null=True,blank=True, related_name='project_manager')
    admin             = models.ForeignKey(UserProfile,on_delete=models.SET_NULL,null=True, related_name='admin')

    def __str__(self):
        return self.user.username

class Task(models.Model):
    title              = models.CharField(max_length=255)
    description        = models.TextField()
    creator            = models.ForeignKey(ProjectManager,on_delete=models.SET_NULL, null=True,related_name='task_author')
    developer_assigned = models.ForeignKey(Developer,on_delete=models.SET_NULL, null=True,blank=True,related_name='task_developer')
    date_created       = models.DateField(auto_now_add=True)
    date_assigned      = models.DateField(auto_now_add=True)
    date_completed     = models.DateField(auto_now_add=True)
    status           = models.CharField(max_length=255)
    priority         = models.CharField(max_length=255)
    project          = models.CharField(max_length=255)
    

class Priority(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Status(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


# class Project(models.Model):
#     pass


# class Ticket(models.Model):
#     pass
    # title = models.CharField(max_length=150)
    # description = models.TextField()
    # priority = 
    # status = 
    # project = 
    # date_created = 
    # date_resolved = 
    # assigned_to = 