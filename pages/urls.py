from . import views
from django.urls import path
app_name = 'pages'
urlpatterns = [
    path('',views.Homepage.as_view(),name="homepage"),
    path('accounts/profile/',views.myprofile,name="myprofile"),
]