
from django.urls import path
from . import views

urlpatterns = [
    path('hr_base',views.hr_base,name='hr_base'),
    path('hr_alldata',views.hr_alldata,name='hr_alldata'),
    path('hr_newdata',views.hr_newdata,name='hr_newdata'),
    path('hr_waitlist',views.hr_waitlist,name='hr_waitlist'),
    path('hr_wastedata',views.hr_wastedata,name='hr_wastedata'),
    path('hr_password',views.hr_password,name='hr_password'),
    path('hr_logout',views.hr_logout,name='hr_logout'),


    path('hr_passwordupdate',views.hr_passwordupdate,name='hr_passwordupdate'),
    path('hr_profileupdate',views.hr_profileupdate,name='hr_profileupdate'),
    path('add_response/<int:pk>',views.add_response,name='add_response'),
    path('add_to_waitingList/<int:pk>',views.add_to_waitingList,name='add_to_waitingList'),
    path('add_to_wastedata/<int:pk>',views.add_to_wastedata,name='add_to_wastedata'),
    path('add_response_from_waitinglist/<int:pk>',views.add_response_from_waitinglist,name='add_response_from_waitinglist'),


]
 