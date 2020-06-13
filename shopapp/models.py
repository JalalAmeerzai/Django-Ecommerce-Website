from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length = 50)
    category = models.CharField(max_length = 50, default="")
    subcategory = models.CharField(max_length = 50, default="")
    price = models.IntegerField(default = 0)
    desc = models.CharField(max_length = 300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shopapp/images', default = "")

    def __str__(self):
        return self.product_name



class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    sender_name = models.CharField(max_length = 50, null=True)
    sender_email = models.CharField(max_length = 50, null=True)
    sender_phone = models.CharField(max_length = 50, null=True)
    msg_desc = models.CharField(max_length = 2000, null=True)

    def __str__(self):
        return self.sender_name + " - "+self.msg_desc[0:50]+"..." 