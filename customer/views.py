from django.shortcuts import render
from . models import CustomerHouseHold
from django.views.generic import ListView,DetailView

class CustomersListView(ListView):
    model = CustomerHouseHold
    paginate_by = 8
    context_object_name = "customers"
    template_name = "customers/index.html"

class CustomerDetailView(DetailView):
    model = CustomerHouseHold
    template_name = 'customers/details.html'
# Create your views here.
