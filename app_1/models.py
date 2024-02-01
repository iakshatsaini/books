from django.db import models

# Create your models here.

class bookList(models.Model):
    id = models.IntegerField(primary_key=True)
    bookName = models.CharField(max_length = 255)
    authorName = models.CharField(max_length = 255)
    bookDescription = models.CharField(max_length = 255)
    
    # def __str__(self):
    #     return f'{self.fname}'