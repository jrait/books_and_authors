from django.db import models

# Create your models here

class Books(models.Model):
    title = models.CharField(max_length = 255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # authors related field from Books
    
    def __repr__(self):
        return f"{self.title}"

class Authors(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    books = models.ManyToManyField(Books,related_name = 'authors')
    notes = models.TextField()
    
    def __repr__(self):
        return f"{self.first_name} {self.last_name}"