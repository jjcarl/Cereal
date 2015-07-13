from django.contrib import admin
from main.models import Cereal, CerealMaker

# Register your models here.


class CerealAdmin(admin.ModelAdmin):
    list_display = ("name", "sugars", )
    search_fields = ["name"]


class CerealInLine(admin.TabularInline):
    model = Cereal


class CerealMakerAdmin(admin.ModelAdmin):
    list_display = ['manufacturer']
    search_fields = ["manufacturer"]
    inlines = [CerealInLine]


admin.site.register(Cereal, CerealAdmin)
admin.site.register(CerealMaker, CerealMakerAdmin)
