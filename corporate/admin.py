from django.contrib import admin

# Register your models here.


from .models import Colleges, TechnicalTraining

admin.site.register(Colleges)

admin.site.register(TechnicalTraining)