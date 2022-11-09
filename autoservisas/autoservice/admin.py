from django.contrib import admin
from . import models

class CarAdmin(admin.ModelAdmin):
    list_display = ('client', 'car_model', 'license_plate', 'vin_code',)
    list_filter = ('car_model', "client")
    search_fields = ('license_plate', 'vin_code')


class OrderEntryInLine(admin.TabularInline):
    model = models.OrderEntry
    extra = 0
    can_delete = False


class OrderAdmin(admin.ModelAdmin):
    list_display = ('car', 'date')
    inlines = (OrderEntryInLine, )
    readonly_fields = ('date',)

    fieldsets = (
        ('Car', {'fields':('car',)}),
        ('Date', {'fields':('date',)}),
    )


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'price')


class OrderEntryAdmin(admin.ModelAdmin):
    list_display = ('service', 'quantity', 'order', 'price')
    list_filter = ('order', )


admin.site.register(models.Car, CarAdmin)
admin.site.register(models.CarModel)
admin.site.register(models.Service, ServicesAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.OrderEntry, OrderEntryAdmin)

