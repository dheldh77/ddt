from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    job = models.CharField(max_length=200)


class Post(models.Model):
    post_id = models.IntegerField(primary_key=True)
    department = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)
    tags = models.TextField()
    contents = models.TextField()


class ViewLog(models.Model):
    post_id = models.OneToOneField(Post, on_delete=models.CASCADE)
    emp_id = models.OneToOneField(Employee, on_delete=models.CASCADE)
    log_time = models.DateTimeField(auto_created=True)


class SearchLog(models.Model):
    emp_id = models.OneToOneField(Employee, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=200)
    log_time = models.DateTimeField(auto_created=True)