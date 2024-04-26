from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView, name='home'),
    path('about/', AboutView, name='about'),
    path('blog/', BlogView, name='blog'),
    path('portfolio/', PortfolioView, name='portfolio'),
    path('contact/', ContactView, name='contact'),
    path('success/', success_view, name='success'),
]
