from django.db import models

# Create your models here.
class Emp(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length = 200, default = name)
    emp_id = models.CharField(max_length=200)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=200)
    working = models.BooleanField(default=True)
    department = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
    
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True, editable = False)
    is_completed = models.BooleanField(default = False)
    
    def __str__(self):
        return self.title
    
    
class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    testimonial = models.TextField()
    picture = models.ImageField(upload_to = "testimonials/")
    rating = models.IntegerField()
    
    def __str__(self):
        return self.testimonial
