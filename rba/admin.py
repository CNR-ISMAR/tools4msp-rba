from django.contrib import admin
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)
from django import forms
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from .models import (CS, CSphase2, Phase2Pressures
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
    FieldPanel("phase2", widget=forms.CheckboxSelectMultiple),
    ] 
modeladmin_register(CSAdmin)

class CSphase2Admin(ModelAdmin):
    model = CSphase2
    menu_label = "Phase 2"
    menu_icon = "success"
    menu_order = 800
    add_to_settings_menu = False 
    exclude_from_explorer = False
    list_display = ("title", "condition_type")
    search_field = ("title", "condition_type")

    panels =[
    FieldPanel("condition_type"),
    FieldPanel("title"),
    FieldPanel("description"),
    FieldPanel("main_pressures_effects"),
    # FieldPanel("pressure_list", widget=forms.CheckboxSelectMultiple),
    InlinePanel("phase2pressures_objects"),
    FieldPanel("main_source_effects"),
    InlinePanel("phase2uses_objects"),
    FieldPanel("use_list", widget=forms.CheckboxSelectMultiple),
    FieldPanel("main_environmental_responses"),
    FieldPanel("env_list", widget=forms.CheckboxSelectMultiple),
    ] 
modeladmin_register(CSphase2Admin)
