from django.contrib import admin
from .models import appuser,area_of_interest,expertise_area,question,answer
# Register your models here.
admin.site.register(appuser)
admin.site.register(expertise_area)
admin.site.register(question)
admin.site.register(answer)
admin.site.register(area_of_interest)