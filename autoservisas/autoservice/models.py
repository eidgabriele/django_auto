from django.db import models
from datetime import date
# Create your models here.


class Service(models.Model):
    service_name = models.CharField('service_name', max_length = 50)
    price = models.DecimalField('price', max_digits =10, decimal_places =2)
    
    def __str__(self) -> str:
        return f"{self.service_name} {self.price}"
    
    class Meta:
        ordering = ['service_name']
        verbose_name = 'service'
        verbose_name_plural = 'services'


class CarModel(models.Model):
    YEARS_CHOICES = ((metai, str(metai)) for metai in reversed(range(1899, date.today().year+1)))
    make = models.CharField('make', max_length = 50)
    car_model = models.CharField('car_model', max_length = 50)
    year = models.IntegerField('year', choices=YEARS_CHOICES)
    engine = models.CharField('engine', max_length = 50)

    def __str__(self) -> str:
        return f"{self.make} {self.car_model} ({self.year}) {self.engine}"
    
    class Meta:
        ordering = ['make', 'car_model']
        verbose_name = "car model"
        verbose_name_plural = "car models"


class Car(models.Model):
    license_plate = models.CharField('license_plate', max_length=10)
    car_model = models.ForeignKey(CarModel, on_delete= models.CASCADE, related_name='cars', )
    vin_code = models.CharField('vin_code', max_length = 20)
    client = models.CharField('client', max_length= 250)

    def __str__(self) -> str:
        return f"{self.license_plate}, {self.car_model.car_model}, {self.client}"

    class Meta:
        ordering = ['client', 'license_plate']
        verbose_name = 'car'
        verbose_name_plural = 'cars'


class Order(models.Model):
    date = models.DateField('date', auto_now_add=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='car', related_name='orders')
    total = models.DecimalField('total', max_digits = 10, decimal_places = 2, default= 0)

    def get_total(self):
        total = 0
        for line in self.order_lines.all():
            total += line.total
        return total
    
    def save(self, *args, **kwargs):
        if not self._state.adding:
            self.total = self.get_total()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.date}: {self.total}"


class OrderEntry(models.Model):
    service = models.ForeignKey(Service, on_delete= models.CASCADE, verbose_name= 'service', related_name='order_lines')
    order = models.ForeignKey(Order, on_delete= models.CASCADE, verbose_name= 'order', related_name='order_lines')
    quantity = models.IntegerField('quantity', default=1)
    price = models.DecimalField('price', max_digits =10, decimal_places =2)

    @property
    def total(self):
        return self.quantity * self.price
        
    def __str__(self) -> str:
        return f"{self.service.service_name}, {self.quantity} x {self.price}"

    class Meta:
        verbose_name = 'order entry'
        verbose_name_plural = 'order entries'