from django.shortcuts import render
from .models import Producto, Tipo
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.

def index(request):
    prod = Producto.objects.all()
    
    # prod_tipo_roll = Producto.objects.filter(tipop__exact='ro').count()
    # prod_tipo_pro = Producto.objects.filter(tipop_exact='pr').count()
    # prod_tipo_pos = Producto.objects.filter(tipop_exact='po').count()

    return render(
        request,
        'index.html',
        context={'Producto':prod},
    )

    # , 'Rolls:':prod_tipo_roll,'Promociones':prod_tipo_pro,'Postres':prod_tipo_pos

class ProdListView(generic.ListView):
    model = Producto

class ProdDetailView(generic.DetailView):
    model = Producto

class ProdCreate(CreateView):
    model = Producto
    fields = '__all__'

class ProdUpdate(UpdateView):
    model = Producto
    fields = '__all__'

class ProdDelete(DeleteView):
    model = Producto
    success_url = reverse_lazy('prod')