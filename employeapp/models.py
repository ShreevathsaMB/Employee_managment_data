from django.db import models

class Employee(models.Model):
   
    
    
    profile = models.ImageField(upload_to='Profile.images/', null=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=(('M', 'Male'), ('F', 'Female')))
    years_of_experience = models.PositiveIntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    company = models.CharField(max_length=100)
    doj = models.DateField(null=True) 

    def __str__(self):
        return self.name
