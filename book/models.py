from django.db import models



class Book(models.Model):
    Name=models.CharField(max_length=100)
    
    
    def __str__(self) :
        return self.Name
