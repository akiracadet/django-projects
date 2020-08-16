from config.settings import DEBUG
from django.contrib import admin
from django.urls import include
from django.urls import path


urlpatterns = [
    path('', include('landing.urls'))
]


if DEBUG:
    urlpatterns += [path('admin/', admin.site.urls)]
