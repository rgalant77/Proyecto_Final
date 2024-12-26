from django.contrib import admin
from productos.models import Snowboard, Ski, Antiparras


# Register your models here.

#admin.site.register(Snowboard)
@admin.register(Snowboard)
class snowboardAdmin (admin.ModelAdmin):
    list_display = ["id", "marca", "modelo", "tamaño", "color"]
    ordering = ("marca", "modelo")
    search_fields = ("marca", "modelo","tamaño")
    list_editable = ["marca"]
    list_filter = ("marca",)
    




#admin.site.register(Ski)
@admin.register(Ski)
class skidAdmin (admin.ModelAdmin):
    list_display = ["id", "marca", "modelo", "tamaño", "color"]
    ordering = ("marca", "modelo")
    search_fields = ("marca", "modelo","tamaño")
    list_editable = ["marca"]
    list_filter = ("marca",)



#admin.site.register(Antiparras)
@admin.register(Antiparras)
class antiparrasAdmin (admin.ModelAdmin):
    list_display = ["id", "marca", "talle", "modelo", "color"]
    ordering = ("marca", "modelo")
    search_fields = ("marca", "modelo")
    list_editable = ["marca"]
    list_filter = ("marca",)
