from django.contrib import admin
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from .models import (CS,
)

class CSAdmin(ModelAdmin):
    model = CS
    menu_label = "Case Study"
    menu_icon = "tick"
    menu_order = 700
    add_to_settings_menu = False 
    exclude_from_explorer = False
    list_display = ("title",)
    search_field = ("title",)

    panels =[
    FieldPanel("title"),
    FieldPanel("description"),
    ImageChooserPanel("image"),
    FieldPanel("map_embed_url"),
    FieldPanel("es_type"),
    FieldPanel("study_area"),
    ] 
modeladmin_register(CSAdmin)