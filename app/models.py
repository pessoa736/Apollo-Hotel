from django.db import models

# Create your models here.

# Model das postagens do blog
class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=119)
    image = models.ImageField(upload_to='posts/')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']  
    
    def __str__(self):
        return self.title
    
class Reservation(models.Model):
    type_of_room_choices = [
        ('casal', 'Casal'),
        ('solteiro', 'Solteiro'),
        ('Suite Princes', 'Suite Princes'),
        ('suite', 'Suite'),
    ]
    
    name = models.CharField(max_length=100)
    check_in = models.DateField()
    check_out = models.DateField()
    type_of_room = models.CharField(max_length=20, choices=type_of_room_choices)
    adult = models.IntegerField(default=0)      
    child = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    