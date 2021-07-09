from django.db.models.query import QuerySet
from django.http import request
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Products, Order, Seccion
from django.db.models import Q
from django.urls import reverse
from .forms import CustomUserCreationForm, ProductsForm
from django.contrib.auth import authenticate, login
from django.contrib import  messages


# Create your views here

def index(request):

    product_cards = Products.objects.order_by('-id')[0:3]
    product_list = Products.objects.order_by('-id')[3:]

    queryset = request.GET.get("item_name")
    product_objects = Products.objects.all()
    if queryset:
        product_cards = Products.objects.filter(
            Q(title__icontains = queryset) |
            Q(description__icontains = queryset)
        ).distinct()
    
    queryset = request.GET.get("category_name")
    if queryset:
        product_cards = Products.objects.filter(
            Q(category__icontains = queryset)
        ).distinct()
    
    return render(request,'shop/index.html',{'product_cards':product_cards,'product_list':product_list,'product_objects':product_objects,        "lista_secciones": Seccion.objects.all(),"lista_articulos": Products.objects.all(),})

def detail(request,id):
    product_object = Products.objects.get(id=id)
    return render(request,'shop/detail.html',{'product_object':product_object})

def checkout(request):

    if request.method == "POST":
        items = request.POST.get('items','')
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        address = request.POST.get('address',"")
        city = request.POST.get('city',"")
        state = request.POST.get('state',"")
        zipcode = request.POST.get('zipcode',"")
        total = request.POST.get('total',"")
    
        order = Order(items=items,name=name,email=email,address=address,city=city,state=state,zipcode=zipcode,total=total)
        order.save()

    return render(request,'shop/checkout.html')

def agregar_producto(request):

    data = {
        'form': ProductsForm()
    }

    if request.method == 'POST':
        formulario = ProductsForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Producto guardado"
        else:
            data["form"] = formulario

    return render(request, 'shop/producto/agregar.html',data)

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="index")
        data["form"] = formulario
    return render(request, 'registration/registro.html',data)

def filtro_secciones(request, seccion_id):
    una_seccion = get_object_or_404(Seccion, id=seccion_id)
    queryset = Products.objects.all()
    queryset = queryset.filter(seccion=una_seccion)
    return render(request,"shop/index.html", {
        "product_cards": queryset,
        "lista_secciones": Seccion.objects.all(),
        "seccion_seleccionada": una_seccion
    })

def modificar_producto(request, id):
        
    productom = get_object_or_404(Products, id=id)

    data = {
        'form':ProductsForm(instance=productom)
    }

    if request.method == 'POST':
        formulario = ProductsForm(data=request.POST, instance=productom, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="index")
        data["form"] = formulario

    return render(request, 'shop/producto/modificar.html', data)

def eliminar_producto(request, id):
    producto = get_object_or_404(Products, id=id)
    producto.delete()
    return redirect(to="index")

def acerca(request):
    return render(request, 'shop/acerca.html')