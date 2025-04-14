from django.contrib import admin
from django.urls import path
from vendas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vendas', views.vendas),
]
