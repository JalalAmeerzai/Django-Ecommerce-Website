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


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000, default="")
    name = models.CharField(max_length=90, default="")
    email = models.CharField(max_length=111, default="")
    address = models.CharField(max_length=111, default="")
    city = models.CharField(max_length=111, default="")
    state = models.CharField(max_length=111, default="")
    zip_code = models.CharField(max_length=111, default="")
    phone = models.CharField(max_length=111, default="")

    def __str__(self):
        return "Order# "+str(self.order_id) + " - "+self.name


class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return "Order# "+str(self.order_id)+" - "+self.update_desc[0:20] + "..."