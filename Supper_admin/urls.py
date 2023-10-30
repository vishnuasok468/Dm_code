from django.urls import path,re_path   
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve


urlpatterns = [
   
    # Super Admin Module --------------------------------

    path('Super-Admin-Dashboard',views.supper_admin_dashboard,name='supper_admin_dashboard'),
    path('Super-Admin-Logout',views.super_admin_logout,name='super_admin_logout'),

    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)