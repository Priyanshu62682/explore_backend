from django.contrib import admin
from .models import appuser,area_of_interest,expertise_area,question,answer,who_answered_what,who_asked_what,q_like,a_like,q_dislike,a_dislike
# Register your models here.
admin.site.register(appuser)
admin.site.register(expertise_area)
admin.site.register(question)
admin.site.register(answer)
admin.site.register(area_of_interest)
admin.site.register(who_answered_what)
admin.site.register(who_asked_what)
admin.site.register(q_like)
admin.site.register(q_dislike)
admin.site.register(a_like)
admin.site.register(a_dislike)
