from django.db import models

# Create your models here.
class PostModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=300)
    post_image = models.ImageField(upload_to="images/")
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    

class PortfolioModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    portfolio_image = models.ImageField(upload_to="images/")
    project_link = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title