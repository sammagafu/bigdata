from django.urls import path
from . import views
app_name = 'transformer'
urlpatterns = [
    path('',views.TransformerListView.as_view(),name="home")
]