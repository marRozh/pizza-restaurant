from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
    path("addsize", views.addsize, name="addsize"),
    path("addsizecheese", views.addsizecheese, name="addsizecheese"),
    path("addsizetop", views.addsizetop, name="addsizetop"),
    path("addsizepizza", views.addsizepizza, name="addsizepizza"),
    path("shoppingcart", views.shoppingcart, name="shoppingcart"),
    path("confirmorder", views.confirmorder, name="confirmorder"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("complete", views.complete, name="complete"),
    path("orders", views.orders, name="orders"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]
