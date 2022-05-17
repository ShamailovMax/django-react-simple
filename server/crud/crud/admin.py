from django.contrib import admin
from crud.models import DetailsModel


# админка
class DetailsAdmin(admin.ModelAdmin):
    pass


admin.site.register(DetailsModel, DetailsAdmin)