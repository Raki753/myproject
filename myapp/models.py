from django.db import models

# Create your models here.
class student(models.Model):
    name=models.TextField(max_length=20)
    age=models.IntegerField()

    def __str__(self):
        return self.name+" "+str(self.age)
    
class Game(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField()
    def __str__(self):
        return self.name    