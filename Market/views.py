from django.shortcuts import render
from django.views.generic import TemplateView,View


# a view for home

class HomeView(TemplateView):
    template_name="home.html"
    
    


#a view for market 
class MarketView(TemplateView):
    template_name="Market/market.html"
    
    
    
#a view for product information
class ProductView(TemplateView):
    template_name="Market/product.html"
    
    

    
    
class AboutView(TemplateView):
    template_name="About.html"
    
    
    
    


