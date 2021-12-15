from django.urls import path

from . import views

app_name = 'pybo' # 추후 다른 앱의 URL별칭과 겹칠 수 있으므로 네임스페이스를 의미하는 app_name 변수 지정

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
]