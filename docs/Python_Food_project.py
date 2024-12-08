Admin py
from django.contrib import admin
from .models import Item
# Register your models here.
admin.site.register(Item)
forms py
from django import forms
from .models import Item
 
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name','item_desc','item_price','item_image']
 
 
models py
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Item(models.Model):
 
    def __str__(self):
        return self.item_name
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,default="")
    
    # delete this afterwards
    def get_absolute_url(self):
           return reverse("food:detail", kwargs={"pk": self.pk})
 
urls py (food)
 
from . import views
from django.urls import path
 
app_name = 'food'  
urlpatterns = [
    #/food/
    path('',views.IndexClassView.as_view(),name='index'),
    #/food/1
    path('<int:pk>/',views.FoodDetail.as_view(),name='detail'),
    path('item/',views.item,name='item'),
    # add items
    
   
    path('add',views.CreateItem.as_view(),name='create_item'),
    # edit
    path('update/<int:id>/',views.update_item,name='update_item'),
    #delete
    path('delete/<int:id>/',views.delete_item,name='delete_item'),
]    
 
views py
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
# Create your views here.
 
 
 
 
def index(request):
    item_list = Item.objects.all()
    
    context ={
        'item_list':item_list,
    }
    return render(request,'food/index.html',context)
 
class IndexClassView(ListView):
    model = Item;
    template_name ='food/index.html'
    context_object_name ='item_list'
 
 
 
 
def item(request):
    return HttpResponse('<h1>This is an item view</h1>')
 
def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    context ={
        'item':item,
    }
 
    return render(request,'food/detail.html',context)
 
class FoodDetail(DetailView):
    model = Item
    template_name = 'food/detail.html'
 
#
def create_item(request):
    form = ItemForm(request.POST or None)
 
    if form.is_valid():
        form.save()
        return redirect('food:index')
 
    return render(request,'food/item-form.html',{'form':form})
 
# this is a class based view for create item
 
class CreateItem(CreateView):
    model = Item;
    fields = ['item_name','item_desc','item_price','item_image']
    template_name='food/item-form.html'
 
    def form_valid(self,form):
        form.instance.user_name = self.request.user
 
        return super().form_valid(form)
      
 
def update_item(request,id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
 
    if form.is_valid():
        form.save()
        return redirect('food:index')
 
    return render(request,'food/item-form.html',{'form':form,'item':item})
 
def delete_item(request,id):
    item = Item.objects.get(id=id)
 
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
 
    return render(request,'food/item-delete.html',{'item':item})
 
 
urls py (mysite)
from django.contrib import admin    
from django.urls import include,path
from users import views as user_views
from django.contrib.auth import views as authentication_views
from django.conf import settings
from django.conf.urls.static import static
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('food/',include('food.urls')),
    path('register/',user_views.register,name='register'),
    path('login/',authentication_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',authentication_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('profile/',user_views.profilepage,name='profile'),
]
 
urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
Template files:
base html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
        <link rel="stylesheet" href="{% static 'food/style.css' %}">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    
    <title>Document</title>
</head>
<body>
    
        <nav class="navbar navbar-dark bg-dark">
                <a href="#" class="navbar-brand">FoodApp</a>
        
                <div class="navbar">
                    <a class="nav-item nav-link" href="{% url 'food:create_item' %}">Add Item</a>
                    <a class="nav-item nav-link" href="#">Delete Item</a>
                    <a class="nav-item nav-link" href="#">View Item</a>
                    {% if user.is_authenticated %}
                        <a href="{% url 'logout' %}">Logout</a>
                        <a href="{% url 'profile' %}">Profile</a>
                    {% else %}
                        <a href="{% url 'login' %}">Login</a>
                    {% endif %}
                </div>
            </nav>
          {% if messages %}
            {% for message in messages %}
            <div class="alert alert-{‌{ message.tags }}">
                    {‌{ message }}
            </div>
                
            {% endfor %}
          {% endif %}
    {% block body %}
    {% endblock %}
</body>
</html>
 
detail html
{% extends 'food/base.html' %}
 
{% block body %}
 
<div class="container">
    <div class="row m-5">
        <div class="col-md-6">
            <img height="300px" src="{‌{ item.item_image }}" class="card"/>
        </div>
 
        <div class="col-md-6">
            <h1>{‌{ object.item_name }}</h1>
            <h2>{‌{ object.item_desc }}</h2>
            <h3>${‌{ object.item_price }}</h3>  
            <a class="btn btn-danger" href="{% url 'food:delete_item' item.id %}">Delete</a>
        </div>
    </div>
</div>
{% endblock %}    
 
 
 
index html
 
 
{% extends 'food/base.html' %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    </head>
<body>
 
    {% block body %}
 
    {% for item in item_list %}
        <div class="row m-5">
            <div class="col-md-3 offset-md-2">
                <img class="card" height="150px" src="{‌{ item.item_image }}"/>
            </div>
            <div class="col-md-4">
                <h3>{‌{ item.item_name }}</h3>
                <h5>{‌{ item.item_desc }}</h5>
                <h6>${‌{ item.item_price }}</h6>
                Added By:<h6>{‌{ item.user_name }}</h6>
 
                <!--delete this later-->
                
                <!---->
            </div>
            <div class="col-md-2">
                <a href="{% url 'food:detail' item.id %}" class="btn btn-success">Details</a>
            </div>
        </div>
        <div class="row">
            <div class="offset-md-2 col-md-8">
                <hr>
            </div>
        </div>
 
    {% endfor %}
    {% endblock %}    
 
    this is the old code
    
   
    <ul>
        <li>
           
            <a href=""> {‌{ item.id }} -- {‌{ item.item_name }}</a>
        </li>
    </ul>
 
       
 
</body>
</html>
 
item-delete html
<form method="POST"">
    {% csrf_token %}
    <h2>Are you sure you want to delete {‌{ item.item_name }}</h2>
    <button type="submit">Confirm</button>
</form>
item-form html
{% extends 'food/base.html' %}
 
{% block body %}
 
<div class="container">
    <div class="row">
        <div class="col-md-4 offset-md-4">
            <div class="card">
                <div class="card-header text-white bg-info">
                    <div class="card-title">
                        Add item
                    </div>
                </div>
                <div class="card-body">
                    <form method="POST">
                        {% csrf_token %}
                        {‌{ form }}
 
                        <button class="btn-info" type="submit">Add</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
 
</div>
{% endblock %}
