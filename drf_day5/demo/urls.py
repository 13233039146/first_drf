from django.urls import path
from demo import views

urlpatterns = [
    path('user/', views.UserAPIView.as_view()),
    path("user_per/",views.UserPermissionAPI.as_view()),

]
