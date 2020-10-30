from django.urls import path
from dangdang import views
# Create your views here.

urlpatterns = [
    path('book/',views.BookAPIView.as_view()),
    path('book/<str:id>/',views.BookAPIView.as_view()),
]