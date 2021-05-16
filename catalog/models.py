from django.db import models

# Create your models here.

class MyModel(models.Model):
    '''A typical class defining model'''
    title = models.CharField(max_length=255)
    field_name = models.CharField(max_length=255, help_text="Input here:")

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title', '-field_name']