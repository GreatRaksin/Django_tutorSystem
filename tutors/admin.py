from django.contrib import admin
from .models import Tutor, Subjects, Cities


class TutorAdmin(admin.ModelAdmin):
    list_display = ('l_name', 'f_name', 'city', 'subject', 'school')
    list_filter = ('city', 'subject', 'school')


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Tutor, TutorAdmin)
admin.site.register(Cities, CityAdmin)
admin.site.register(Subjects, SubjectAdmin)