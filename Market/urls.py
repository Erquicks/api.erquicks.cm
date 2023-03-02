from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view() ,name="home"),
    path('market/',views.MarketView.as_view(),name="market"),
    path('product/<id>',views.ProductView.as_view(),name="product"),
]