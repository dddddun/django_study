from django.contrib import admin
from django.urls import path, include
from app_name.views import base_views


urlpatterns = [
    # '/'에 해당되는 path
    path('', base_views.index, name='index'),
    path('app_name/', include('app_name.urls')),
    path('admin/', admin.site.urls),
    path('common/', include('common.urls')),
    path('app_name2/', include('app_name2.urls')),
]
