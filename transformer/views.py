from django.shortcuts import render
from . models import Transformer,TransformerReading
from django.views.generic import ListView,DetailView


class TransformerListView(ListView):
    model = Transformer
    template_name = "transformer/index.html"
    paginate_by = 20
    context_object_name = 'transformer'
