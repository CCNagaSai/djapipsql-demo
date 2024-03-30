from .views import create_data
from django.urls import path

urlpatterns = [
    path('create/', create_data, name='create_data'),

]