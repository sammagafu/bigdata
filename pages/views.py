from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

# Create your views here.
# 
class Homepage(TemplateView):
    template_name = 'pages/home.html'

@login_required
def myprofile(request):
    return render(request,'registration/profile.html')