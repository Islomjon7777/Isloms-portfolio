from django.contrib import admin
from .models import PostModel, PortfolioModel

# Register your models here.
admin.site.register(PostModel)
admin.site.register(PortfolioModel)