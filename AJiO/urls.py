from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("orders/<int:id>", views.index, name="orders"),
    path("orders/", views.NoIdOrders, name="NoIdOrders"),
    path("menu/", views.menu, name="menu"),
    path("menu/<int:id>", views.EditMenu, name="EditMenu"),
]
