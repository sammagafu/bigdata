from . import views
from django.urls import path
app_name = 'pages'
urlpatterns = [
    path('', views.Homepage.as_view(), name="homepage"),
    path('api/customer/',views.ChartData.as_view()),
    path('accounts/profile/',views.myprofile,name="myprofile"),
]