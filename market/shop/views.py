from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse 

def index(request):
    browser_info = request.META['HTTP_USER_AGENT']
    return HttpResponse("Привет! Я знаю много инфы о твоем браузере. {}".format(browser_info))

from django.views import generic 
from .models import Product
from .models import Category

class ProductListView(generic.ListView):
    template_name = 'products_list.html'
    context_object_name = 'products'
    model = Product 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context 

class ProductDetail(generic.DetailView):
    template_name = 'product_detail.html'
    context_object_name = 'products'
    model = Product 

class CategoryListView(generic.ListView):
    template_name = 'category_list.html'
    context_object_name = 'categories'
    model = Category
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context

class CategoryDetail(generic.DetailView):
    template_name = 'category_detail.html'
    context_object_name = 'categories'
    model = Category
