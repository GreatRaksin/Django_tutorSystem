from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple
from .models import Tutor, Subjects, Cities


class TutorAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
    list_display = ('l_name', 'f_name', 'city', 'school')
    list_filter = ('city', 'subject', 'school')


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Tutor, TutorAdmin)
admin.site.register(Cities, CityAdmin)
admin.site.register(Subjects, SubjectAdmin)