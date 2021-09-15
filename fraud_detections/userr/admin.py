from django.contrib import admin
from . models import csvfile,us_data,userfile
# Register your models here.
admin.site.register(csvfile)
admin.site.register(us_data)
admin.site.register(userfile)
