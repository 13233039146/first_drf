from django.urls import path
from drx_first import views

app_name = 'drx_first'

urlpatterns = [
    path('user/',views.UserAPIView.as_view()),
    path('user/<int:id>/',views.UserAPIView.as_view()),

]