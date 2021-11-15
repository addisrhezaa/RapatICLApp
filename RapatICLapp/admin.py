from django.contrib import admin
from RapatICLapp.models import Notulensi, Rapat, Absensi, Asisten

# Register your models here.
admin.site.register(Rapat)
admin.site.register(Absensi)
admin.site.register(Asisten)
admin.site.register(Notulensi)