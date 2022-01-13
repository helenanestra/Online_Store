from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin
from rest_framework import viewsets
from django.contrib.auth.mixins import LoginRequiredMixin
from products.models import Product, Category
from products.serializers import ProductSerializer, CategorySerializer
from django.http import HttpResponseRedirect
from django.shortcuts import render


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'


class ProductCreateView(CreateView, PermissionRequiredMixin):
    permission_required = "products.create_product"
    model = Product
    Product.objects.order_by().filter()
    template_name = 'product_create.html'
    fields = '__all__'
    success_url = reverse_lazy('product_list')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = "products.change_product"
    model = Product
    template_name = 'product_update.html'
    context_object_name = 'product'
    fields = '__all__'
    success_url = reverse_lazy('product_list')


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = "products.delete_product"
    model = Product
    template_name = 'product_delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('product_list')


class ProductViewSet(PermissionRequiredMixin, viewsets.ModelViewSet):
    permission_request = "products.list_product"
    queryset = Product.objects.all().order_by('-name')
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer




def counter(request):
    # Number of visits to this view, stored in the session variable.
    visits_count = request.session.get('visits_count', 0)
    request.session['visits_count'] = visits_count + 1

    context = {
        'visits_count': visits_count
    }

    # Render the HTML template passing data in the context.
    return render(request, 'counter.html', context=context)
