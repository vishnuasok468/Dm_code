from django.urls import path 
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
   
    # TL Module -------Sumayya-------------------------

    path('TL-Dashboard',views.tl_dashboard,name='tl_dashboard'),
    path('TL-Logout',views.tl_logout,name='tl_logout'),

    # Profile ------------------------------

    path('TL-Profile',views.tl_profile,name='tl_profile'),
    path('TL-Profile-Update',views.tl_profile_detailsUpdate,name='tl_profile_detailsUpdate'),
    path('TL-Profile-Image\Remove',views.tl_profileImage_remove,name='tl_profileImage_remove'),

    # Password ----------------------------

    path('TL-Password',views.tl_password,name='tl_password'),
    path('TL-Password-Update',views.tl_user_passwordUpdate,name='tl_user_passwordUpdate'),

    # Feedback  --------------------------

    path('TL-Feedback',views.tl_feedback,name='tl_feedback'),
    path('TL-Add-Feedback',views.tl_add_feedback,name='tl_add_feedback'),
    path('TL-Filter-Feedback',views.tl_filter_feedback,name='tl_filter_feedback'),

    # Complaints --------------------------

    path('TL-Complaints',views.tl_complaints,name='tl_complaints'),
    path('TL-Complaints-Action',views.tl_complaints_action_taken,name='tl_complaints_action_taken'),

    # Action Taken  --------------------------

    path('TL-Action-Taken',views.tl_actionTaken,name='tl_actionTaken'),
    path('TL-ActionTakenSave',views.tl_action_taken_save,name='tl_action_taken_save'),
    path('TL-ActionTakenEditPage\<int:act_id>',views.tl_action_taken_editPage,name='tl_action_taken_editPage'),
    path('TL-ActionTakenEdit\<int:aid>',views.tl_action_takenEdit,name='tl_action_takenEdit'),

    # Leave ---------------------------
    
    path('TL-Leave',views.tl_leave,name='tl_leave'),
    path('TL-Leave-Apply',views.tl_leave_apply,name='tl_leave_apply'),
    path('TL-Filter-Leave',views.tl_filter_leaves,name='tl_filter_leaves'),
    path('TL-Filter-Leave-Emp',views.tl_filter_leaves_emp,name='tl_filter_leaves_emp'),

    # Notification ----------------------

    path('TL-Notification',views.tl_allnotification,name='tl_allnotification'),
    path('TL-Open-Notification\<int:n_id>',views.tl_open_notification,name='tl_open_notification'),
    path('TL-Delete-Notification\<int:n_id>',views.tl_delete_notification,name='tl_delete_notification'),

     #Schedule ----------------------------

    path('TL-Schedule',views.tl_schedule,name='tl_schedule'),
    path('TL-schedule-Tasks',views.tl_schedule_tasks,name='tl_schedule_tasks'),
    path('TL-schedule-Edit-Page\<int:sch_id>',views.tl_edit_schedulePage,name='tl_edit_schedulePage'),
    path('TL-schedule-Edit\<int:taskid>',views.tl_edit_schedule,name='tl_edit_schedule'),
    path('TL-schedule-Delete\<int:taskid>',views.tl_delete_schedule,name='tl_delete_schedule'),
    path('TL-schedule-Status',views.tl_update_schedule_status,name='tl_update_schedule_status'),
    path('TL-Filter-schedule',views.tl_filter_schedule,name='tl_filter_schedule'),

    path('TL-Employees-schedule',views.tl_employees_schedule,name='tl_employees_schedule'),
    path('TL-Employees-schedule-add',views.tl_schedule_emp_tasks,name='tl_schedule_emp_tasks'),
    path('TL-Employees-schedule-Edit-Page\<int:sch_id>',views.tl_edit_emp_schedulePage,name='tl_edit_emp_schedulePage'),
    path('TL-Employees-schedule-Edit\<int:taskid>',views.tl_edit_emp_schedule,name='tl_edit_emp_schedule'),
    path('TL-Employees-schedule-delete\<int:taskid>',views.tl_delete_emp_schedule,name='tl_delete_emp_schedule'),
    path('TL-Employees-schedule-filter',views.tl_emp_filter_schedule,name='tl_emp_filter_schedule'),

    #Employees Section----------------------------

    path('TL-Employees',views.tl_employee_section,name='tl_employee_section'),
    path('TL-Employees-View',views.tl_view_employees,name='tl_view_employees'),
    path('TL-Employees-Progress',views.tl_WorkProgress,name='tl_WorkProgress'),
    path('TL-Employees-Leaves',views.tl_employee_leaves,name='tl_employee_leaves'),
    path('TL-Employees-Filter-Leave',views.tl_emp_filter_leaves,name='tl_emp_filter_leaves'),
    path('TL-Employees-Schedules',views.tl_employee_schedules,name='tl_employee_schedules'),
    path('TL-Employees-Filter-Schedules',views.tl_emp_filter_schedules,name='tl_emp_filter_schedules'),
    path('TL-Employees-ActionTaken',views.tl_employee_actionTaken,name='tl_employee_actionTaken'),
    path('TL-Employees-Filter-ActionTaken',views.tl_emp_filter_actionTaken,name='tl_emp_filter_actionTaken'),
    path('TL-Employees-Feedback',views.tl_employee_feedback,name='tl_employee_feedback'),
    path('TL-Employees-Filter-Feedback',views.tl_emp_filter_feedback,name='tl_emp_filter_feedback'),
     path('TL-Employees-Complaints',views.tl_employee_complaints,name='tl_employee_complaints'),
    path('TL-Employees-Filter-Complaints',views.tl_emp_filter_complaints,name='tl_emp_filter_complaints'),


    

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)