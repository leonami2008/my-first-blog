from django.conf import settings
from django.db import models
from django.utils import timezone

#define nuestro modelo
class Post(models.Model):
#Propiedades
#modelos.ForeignKey, este es una relación (link) con otro modelo.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#models.CharField, así es como defines un texto con un número limitado de caracteres.
    title = models.CharField(max_length=200)
#models.TextField, este es para texto largo sin límite
    text = models.TextField()
    create_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
#def significa que es una función/método
#publish es el nombre del método
    def publish(self):
        self.published_date = timezone.now()
        self.save()

#dos guines en str se llaman "dunder" (abreviatura de "double-underscore" o, en español, "doble guión bajo").
    def __str__(self):
        return self.title