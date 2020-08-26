from django.contrib import admin

from .models import Annotation


class AnnotationAdmin(admin.ModelAdmin):
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name']


admin.site.register(Annotation, AnnotationAdmin)
