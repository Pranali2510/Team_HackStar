from django.db import models

# Create your models here.


class cleanliness_model(models.Model):
    objects = None
    name = models.CharField(default='', max_length=100)
    pnr = models.CharField(default='', max_length=100)
    building_name = models.CharField(max_length=100, default='')
    class_no = models.CharField(default='', max_length=100)
    description = models.CharField(default='', max_length=100)
    cleaned = models.CharField(default='', max_length=100)

    def __str__(self):
        return self.class_no


class contact_model(models.Model):
    name = models.CharField(default='', max_length=100)
    email = models.EmailField(default='', max_length=100)
    message = models.CharField(default='', max_length=100)

    def __str__(self):
        return self.name


class lost_found_model(models.Model):
    name = models.CharField(default='', max_length=100)
    pnr = models.CharField(default='', max_length=100)
    building_name = models.CharField(max_length=100, default='')
    class_no = models.CharField(default='', max_length=100)
    description = models.CharField(default='', max_length=100)
    item = models.CharField(default='', max_length=100)
    image = models.FileField(upload_to='images/', null=True, verbose_name="", default='')
    date_time= models.DateField(default='')
    found = models.CharField(default='', max_length=100)

    def __str__(self):
        return self.class_no


class UserDetails(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    prn_number = models.IntegerField(default=0)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    contact = models.IntegerField(default=0)
    email = models.EmailField(default=True, primary_key=True)
    role = models.CharField(max_length=20, default="User")

    def __str__(self):
        return self.role


# Create your models here.
class Foods(models.Model):
    canteen_name = models.CharField(max_length=100,default="")
    image = models.ImageField(upload_to="pics")
    categeory = models.CharField(max_length=50, default="")
    name = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    def _str_(self):
        return self.name


class Order(models.Model):
    items_json = models.CharField(max_length=1000, default="")
    name = models.CharField(max_length=50, default="")
    time = models.CharField(max_length=20, default="")
    phone = models.IntegerField(default=0)
    tprice = models.CharField(max_length=20, default='')
    status = models.CharField(max_length=20, default='')
    def _str_(self):
        return self.tprice


class EventDetails(models.Model):
    name = models.CharField(max_length=100)
    prn_number = models.IntegerField(default=0, primary_key=True)
    event_name = models.CharField(max_length=100)
    event_dest = models.CharField(max_length=100)
    max_crowd = models.IntegerField(default=0)
    duration = models.DateTimeField()

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=100,default='')
    desc = models.CharField(max_length=1000,default='')
    date = models.CharField(max_length=20,default='')
    register = models.IntegerField(max_length=100,default=0)
    def __str__(self):
        return self.name
    
class Eregister(models.Model):
    name = models.CharField(max_length=100, default='')
    event_id= models.IntegerField(default=0)
    prn = models.CharField(max_length=100, default='')
    course = models.CharField(max_length=100, default='')
    year = models.CharField(max_length=100, default='')
    phone = models.IntegerField(default=0)
