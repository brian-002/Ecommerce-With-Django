from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank= True, null= False )
    date_created = models.DateTimeField(auto_now= True)
    available = models.BooleanField(default=True )

    def __str__(self):
        return self.name
