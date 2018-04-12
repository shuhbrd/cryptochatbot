from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse 
from django.views import generic 

from .models import Product
from .models import Category
from .models import Order
#from .models import User

def index(request):
    browser_info=request.META['HTTP_USER_AGENT']
    return HttpResponse("Привет! Я знаю много инфы о твоем браузере. {}".format(browser_info))

class ProductListView(generic.ListView):
    template_name = 'products_list.html'
    context_object_name = 'products'
    model = Product 
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['category']=Category.objects.all()
        return context 

class ProductDetail(generic.DetailView):
    template_name = 'product_detail.html'
    context_object_name = 'product'
    model = Product 

class CategoryListView(generic.ListView):
    template_name = 'category_list.html'
    context_object_name = 'categories'
    model = Category

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context 

class CategoryDetail(generic.DetailView):
    template_name = 'category_detail.html'
    context_object_name = 'category'
    model = Category

class OrderFormView(generic.CreateView):
    model = Order
    template_name = "order_form.html"
    context_object_name = 'order'
    success_url = '/order/successful/'
    fields = ['customer_name', 'customer_phone']

    def form_valid(self, form):
        product = Product.objects.get(id=self.kwargs['pk'])
        form.instance.product = product
        return super().form_valid(form)

class SuccessfulOrderView(generic.ListView):
    template_name = "successorder_form.html"
    model = Order
    context_object_name = 'successful_order'