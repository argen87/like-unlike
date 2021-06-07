from django.urls import path
from knox import views as knox_views







from . import views
from .views import RegisterAPI,LoginAPI

urlpatterns = [
    path('', views.api_overview_links),
    path('list/', views.get_task_list),
    path('create/', views.task_create),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),


]





