from django.db import models



# Create your models here.
class Event(models.Model):
    # : name, description, date, time, location, category (ForeignKey)
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    category = models.ForeignKey('Category', on_delete=models.CASCADE ,default=None)
    
    def __str__(self):
        return self.name
    
    
class Participent(models.Model):
    #  name, email, and a ManyToMany relationship with Event.
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    events = models.ManyToManyField(Event, related_name='participants')
    
    def __str__(self):
        return self.name
    
    
class Category(models.Model):   
    # name and description.
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name
