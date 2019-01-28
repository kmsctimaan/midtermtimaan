from django.urls import path
from . import views

app_name = 'post'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('update/', views.update, name='update'),
    # path('comment/', views.comment, name='comment'),
    path('create/', views.create, name='create'),
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/update', views.update, name='update'),

]
