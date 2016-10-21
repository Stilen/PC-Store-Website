from django.contrib import admin
from .models import Contact


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ['date']


admin.site.register(Contact, ContactAdmin)
