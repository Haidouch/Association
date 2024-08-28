from django.db import models

# Create your models here.

class Contact(models.Model) :
      name = models.CharField(max_length=100, primary_key=True)
      email = models.CharField(max_length=20)
      content = models.TextField()
      def __str__(self) :
            return self.name

class Resshaumains(models.Model) :
    name = models.CharField(max_length=100, primary_key=True)
    ressourcesdelegation = models.IntegerField()
    ressourcessocial = models.IntegerField()
    def __str__(self):
   	    return self.name

class Revenus(models.Model) :
    partenaire = models.CharField(max_length=100, primary_key=True)
    valeur = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
   	    return self.partenaire

class Depenses(models.Model) :
    type = models.CharField(max_length=100, primary_key=True)
    valeur = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
   	    return self.type
        
class Dettes(models.Model) :
      creancier = models.CharField(max_length=100, primary_key=True)
      montant = models.DecimalField(max_digits=10, decimal_places=2)
      def __str__(self):
        return self.creancier

class DialyseDataYear(models.Model):
    year = models.CharField(max_length=4, primary_key=True)
    nbrPatients = models.IntegerField()
    nbrSessions = models.IntegerField()
    nbrMachines = models.IntegerField()
    def __str__(self):
        return self.year

class CoutDePatients(models.Model) :
    column = models.CharField(max_length=50, primary_key=True)
    y2018 = models.IntegerField()
    y2019 = models.IntegerField()
    y2020 = models.IntegerField()
    y2021 = models.IntegerField()
    def __str__(self):
        return self.column


class Image(models.Model) :
    title = models.CharField(max_length=50, primary_key=True)
    img = models.ImageField(upload_to='imgs/')
    def __str__(self) :
        return self.title
    

class Activitie(models.Model) :
    titre = models.CharField(max_length=50)
    concept = models.CharField(max_length=200)
    image = models.ImageField(upload_to='services/')
    href = models.TextField()
    def __str__(self) :
        return self.titre


class Service(models.Model):
    services = models.ForeignKey(Activitie, on_delete=models.CASCADE)
    titre = models.CharField(max_length=100)
    images = models.ImageField(upload_to='service/')
    description = models.TextField()
    num = models.IntegerField()
    def __str__(self) :
        return self.titre

