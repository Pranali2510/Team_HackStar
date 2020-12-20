from django.contrib import admin
from .models import cleanliness_model,lost_found_model, UserDetails,EventDetails,Event, Eregister,contact_model
from .models import Foods, Order

admin.site.register(UserDetails)
admin.site.register(cleanliness_model)
admin.site.register(lost_found_model)
admin.site.register(EventDetails)
admin.site.register(Foods)
admin.site.register(Order)
admin.site.register(Event)
admin.site.register(Eregister)
admin.site.register(contact_model)