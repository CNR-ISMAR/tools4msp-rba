from django.contrib import admin
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from .models import (CS, CSphase2,
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
    FieldPanel("policy_objectives"),
    FieldPanel("ecosystem_services"),
    FieldPanel("future_scenarios"),
    FieldPanel("phase2"),
    ] 
modeladmin_register(CSAdmin)

class CSphase2Admin(ModelAdmin):
    model = CSphase2
    menu_label = "Phase 2"
    menu_icon = "success"
    menu_order = 800
    add_to_settings_menu = False 
    exclude_from_explorer = False
    list_display = ("title",)
    search_field = ("title",)

    panels =[
    FieldPanel("title"),
    FieldPanel("description"),
    FieldPanel("condition_type"),
    FieldPanel("main_pressures_effects"),
    FieldPanel("pressure_list"),
    FieldPanel("main_source_effects"),
    FieldPanel("main_environmental_responses"),
    ] 
modeladmin_register(CSphase2Admin)