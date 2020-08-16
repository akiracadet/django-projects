from django.urls import path

from landing.views import HomeView
from landing.views import AboutView
from landing.views import ContactView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact')
]
