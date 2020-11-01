from django.urls import path
from view_set import views
urlpatterns = [
    path('api/',views.ManagerApiView.as_view()),
    path('api/<str:id>/',views.ManagerApiView.as_view()),

    path('gen/',views.ManagerGenAPIView.as_view()),
    path('gen/<str:id>/',views.ManagerGenAPIView.as_view()),

    path('gen_mixin/', views.ManagergenAPIView.as_view()),
    path('gen_mixin/<str:id>/', views.ManagergenAPIView.as_view()),

    path('view_set/', views.ManagerViewsetAPIView.as_view({'post':'registe'})),
    # path('view_set/<str:id>/', views.ManagerViewsetAPIView.as_view({'post':'registe'})),
    path('view_set_login/', views.ManagerViewsetAPIView.as_view({'post':'login'})),
]