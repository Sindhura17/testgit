from django.contrib import admin
from .models import doctor
from .models import event
from .models import ngo
from .models import patient
from .models import regis

# Register your models here.
admin.site.register(doctor)
admin.site.register(event)
admin.site.register(ngo)
admin.site.register(patient)
admin.site.register(regis)
