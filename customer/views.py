from django.shortcuts import render
from . models import CustomerHouseHold, Transaction, MetreReading
from django.views.generic import ListView,DetailView

class CustomersListView(ListView):
    model = CustomerHouseHold
    paginate_by = 8
    context_object_name = "customers"
    template_name = "customers/index.html"

class CustomerDetailView(DetailView):
    model = CustomerHouseHold
    template_name = 'customers/details.html'
    context_object_name = 'client'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['transaction'] = Transaction.objects.filter(buyer=self.get_object()).order_by('-date')[:10]
        context['meterreading'] = MetreReading.objects.filter(owner=self.get_object()).order_by('-date')[:10]
        return context


# Create your views here.
# def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['category'] = Category.objects.all()
#         return context