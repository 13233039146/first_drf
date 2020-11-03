from django.urls import path
from rest_framework_jwt.views import ObtainJSONWebToken
from token_app import views
urlpatterns = [
    path('auto_login_check/',ObtainJSONWebToken.as_view()),
    path('query/',views.GetInfo.as_view()),
    path('many_login/',views.LoginManyAPIView.as_view()),
    path('filter/',views.FilterPhone.as_view())
]