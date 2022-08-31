from django.shortcuts import render, redirect
from .models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()

    if request.GET.get('sort') == 'name':
        phones = Phone.objects.order_by('name')
    if request.GET.get('sort') == 'min_price':
        phones = Phone.objects.order_by('price')
    if request.GET.get('sort') == 'max_price':
        phones = Phone.objects.order_by('-price')

    context_dict = {'phones': phones}
    return render(request, template, context_dict)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug = slug)
    context = {'phone': phone}
    return render(request, template, context)
