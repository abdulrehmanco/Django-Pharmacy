from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Company),
admin.site.register(Medicine),
admin.site.register(Bill),
admin.site.register(Employee),
