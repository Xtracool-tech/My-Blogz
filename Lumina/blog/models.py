from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field #type: ignore

choices = [('technology', 'Technology'), ('design', 'Design')]

class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=300, default='Post excerpt')
    content = CKEditor5Field()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    tag = models.CharField(max_length=50, choices=choices, default='TECHNOLOGY')

    def __str__(self):
        return self.title
