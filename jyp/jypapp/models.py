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


class Category(models.Model):
    cate_id = models.IntegerField(primary_key=True, auto_created=True)
    large_category = models.CharField(max_length=200)
    middle_category = models.CharField(max_length=200)
    detail_category = models.CharField(max_length=200)


class ViewLog(models.Model):
    post_id = models.ManyToManyField(Post)
    emp_id = models.ManyToManyField(Employee)
    cate_id = models.ManyToManyField(Category)
    log_time = models.DateTimeField(auto_now=True)


class SearchLog(models.Model):
    emp_id = models.ManyToManyField(Employee)
    keyword = models.CharField(max_length=200)
    log_time = models.DateTimeField(auto_now=True)