from django.urls import path
from dangdang import views
# Create your views here.

urlpatterns = [
    path('book/',views.BookAPIView.as_view()),
    path('book/<str:id>/',views.BookAPIView.as_view()),
    path('gen/<str:id>/',views.BookApiView_mixin.as_view()),
    path('gen/',views.BookApiView_mixin.as_view())
]