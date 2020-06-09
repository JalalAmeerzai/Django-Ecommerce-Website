from django.db import models

# Create your models here.
class Products(models.Model):
    product_id = models.AutoField
    product_namme = models.CharField(max_length = 50)
    desc = models.CharField(max_length = 300)
    pub_date = models.DateField()
