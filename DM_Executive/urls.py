from django.urls import path 
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
   
    # Executive Module --------------------------------

    path('Executive-Dashboard',views.executive_dashboard,name='executive_dashboard'),
    path('Executive-Logout',views.executive_logout,name='executive_logout'),

    # Profile ------------------------------

    path('Executive_Profile',views.executive_profile,name='executive_profile'),
    path('Exprofile-Update',views.Profile_detailsUpdate,name='Profile_detailsUpdate'),
    path('Exprofile-Image\Remove',views.profileImage_remove,name='profileImage_remove'),


    # Password ----------------------------

    path('Expassword',views.executive_password,name='executive_password'),
    path('Expassword-Update',views.user_passwordUpdate,name='user_passwordUpdate'),


    # Action Taken  --------------------------

    path('Executive-Action-Taken',views.executive_actionTaken,name='executive_actionTaken'),

    
    # Notification ----------------------

    path('Executive-Notification',views.executive_allnotification,name='executive_allnotification'),
    path('Exmark-notification/<int:pk>',views.exmark_notification,name='exmark_notification'),
    path('Exdelete-notification/<int:pk>', views.exdelete_notification, name='exdelete_notification'),
    path('Exdelete_selected_notifications', views.delete_selected_notifications, name='delete_selected_notifications'),


    # Feedback  --------------------------

    path('Executive-Feedback',views.executive_feedback,name='executive_feedback'),
    path('Executive-Add-Feedback',views.exadd_feedback,name='exadd_feedback'),
    path('Executive-Feedbackgiven',views.exfeedback_given,name='exfeedback_given'),
    path('Executive-Feedbackreceived',views.exfeedback_received,name='exfeedback_received'),


    # Complaints --------------------------

    path('Executive-Complaints',views.executive_complaints,name='executive_complaints'),
    path('Add-Executive-Complaints',views.addex_complaint,name='addex_complaint'),

    # Leave ---------------------------
    
    path('Executive-Leave',views.executive_leave,name='executive_leave'),
    path('Exapply-leave',views.exapply_leave,name='exapply_leave'),
    path('Filterex-Leave',views.filter_exleave,name='filter_exleave'),


    #Schedule ----------------------------

    path('Executive-Schedule',views.executive_schedule,name='executive_schedule'),
    path('Executive-schedule-remove/<int:pk>',views.executive_scheduleRemove,name='executive_scheduleRemove'),
    path('Executive-schedule-save',views.executive_schedule_save,name='executive_schedule_save'),
    path('Executive-schedule-Edit',views.ScheduleEdit,name='ScheduleEdit'),
    path('Executive-update_schedule_status',views.update_schedule_status,name='update_schedule_status'),
    path('Executive-schedule-View',views.executive_scheduleview,name='executive_scheduleview'),
    path('Executive-schedule-filterday',views.executive_scheduleFilterday,name='executive_scheduleFilterday'),
    path('Executive-filter_schedules', views.filter_schedules, name='filter_schedules'),



]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)