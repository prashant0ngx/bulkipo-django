from django.contrib import admin

from .models import DmatsAccount, Share

# Register your models here.
admin.site.register(DmatsAccount)
admin.site.register(Share)
