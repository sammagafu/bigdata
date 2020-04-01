from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from customer.models import CustomerHouseHold, Transaction
from transformer.models import TransformerReading
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum



# Create your views here.
# 
class Homepage(TemplateView):
    template_name = 'pages/home.html'

@login_required
def myprofile(request):
    users = CustomerHouseHold.objects.count()
    return render(request, 'registration/profile.html', {'users': users})

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        data = Transaction.objects.values('date').annotate(Sum('units'))
        return Response(data)

class TransformerChart(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        data = TransformerReading.objects.all()
        return Response(data)