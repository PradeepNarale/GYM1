from django.contrib import admin
from django.urls import path
from home import views 

urlpatterns = [
    path("",views.index, name='home'),
    path("yoga/",views.yoga, name='yoga'),
    path("sc/",views.sc, name='sc')
]
