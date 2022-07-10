from django.urls import path
from . import views
# from .views import ShowAllProducts

app_name = "products"

urlpatterns = [
    path('', views.index, name = 'index'),
    path("", views.home, name="home"),
    path("addProduct/", views.addProduct, name="addProduct"),
    path('deleteProduct/<int:id>/', views.deleteProduct, name='deleteProduct'),
]