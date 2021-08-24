from django.urls import path

from . import views

app_name = 'app_name'

urlpatterns = [
    # url을 분리하기 전에는 path('app_name/', views.index), 이렇게 생겼었다!
    # app_name/로 시작하는 URL이 config/urls.py 파일과 먼저 매핑되었기 때문에 '' 로 바뀐것!
    # config/urls.py 의 'app_name'  +  app_name/urls의  '' 가 더해져서 최종 URL이 된다.
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
]
