from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Organization(models.Model):
    name=models.CharField(default="erquick organisation", max_length=50)
    
    
    

class Permission(models.Model):
    pass
class Client(models.Model):
    user=models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    
    
#deliver class    
class Deliver(models.Models):
    user=get_user_model()
    
class Partner(models.Models):
    user=models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    organisation=models.OneToOneField(Organization, on_delete=models.CASCADE)
     
     
class Article(models.Model):
    name=models.CharField(default="erquicks item", max_length=50)
    seller=models.OneToOneField(Partner,on_delete=models.CASCADE)
    

class LigneCommande(models.Model):
    qte=models.IntegerField(default=0)
    article= models.ForeignKey(Article,(""), on_delete=models.CASCADE)
    
    
 
class Commande(models.Models):
    user=models.ForeignKey(Client,on_delete=models.CASCADE)
    
    
class Delivery(models.Model):
    deliver=models.ForeignKey(Deliver,on_delete=models.CASCADE)
    

    
    



    
    