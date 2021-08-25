from django.contrib import admin
from django.urls import path, include
from app_name import views
# url 앱 별로 분류하기
# from app_name import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # app_name/ URL이 요청되면 view.index를 호출하라는 매핑
    # view.index는 views.py 파일의 index 함수를 의미한다.
    # path('app_name/', views.index),

    # url 앱 별로 분류하기
    # app_name/ 으로 시작하는 페이지를 요청하면 app_name/urls.py 파일의 매핑 정보를 읽어서 처리해라.

    path('app_name/', include('app_name.urls')),
    path('common/', include('common.urls')),
    # '/'에 해당되는 path
    path('', views.index, name='index'),
]
