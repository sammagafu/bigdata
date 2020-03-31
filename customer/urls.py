from django.urls import path
from . import views
app_name = 'customers'
urlpatterns = [
    path('', views.CustomersListView.as_view(), name="index"),
    path('<int:pk>/',views.CustomerDetailView.as_view(),name="detail")   
]