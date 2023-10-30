
from django.urls import path
from . import views

urlpatterns = [
    path('hr_base',views.hr_base,name='hr_base'),
]
 