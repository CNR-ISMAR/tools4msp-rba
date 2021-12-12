from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from multiselectfield import MultiSelectField

# case study model
class CS(models.Model): 
    title = models.CharField(max_length=400, blank=True, null=False)
    description = RichTextField( null=True, blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    map_embed_url = models.URLField(max_length=600,blank=True, null=True)

    

    #phase1 
    study_area = RichTextField( null=True, blank=True, 
        verbose_name= "1.1 Define the Study Area")

    policy_objectives = RichTextField( null=True, blank=True, 
        verbose_name= "1.2 Define Policy objectives")

    ecosystem_services = RichTextField( null=True, blank=True, 
        verbose_name= "1.3 Define core Ecosystem Services")

    MONITORING_PROGRAM = "Monitoring program"
    PORTAL = "Portal"
    MAP = "Map"
    DATASET = "Dataset"
    DATASOURCE = "Data Source"
    OTHER = "Other"
    
    ES_TYPE_CHOICES = [
        (MONITORING_PROGRAM, 'Monitoring program'),
        (PORTAL, 'Portal'),
        (MAP, 'Map'), 
        (DATASET, 'Dataset'),
        (DATASOURCE, 'Data Source'),
        (OTHER, 'Other')
    ]
    
    es_type = MultiSelectField(choices= ES_TYPE_CHOICES,
        max_choices=5,
        null=True,
        blank=True,
    )

    future_scenarios = RichTextField( null=True, blank=True, 
        verbose_name= "1.4 Define future scenarios")
    
    #phase2 = models.ForeignKey(CS_phase2, on_delete=models.CASCADE)

#phase2
class CS_phase2(models.Model):
    description = RichTextField( null=True, blank=True)

    PRESENT_CONDITION ="Present Condition"
    FUTURE_CONDITION="Future Condition"
    MANAGEMENT_MEASURES="Management Measures"
    
    CONDITION_TYPE_CHOICES = [
        (PRESENT_CONDITION, "Present Condition"),
        (FUTURE_CONDITION, "Future Condition"),
        (MANAGEMENT_MEASURES, "Management Measures")
    ]
    
    condition_type = MultiSelectField(choices= CONDITION_TYPE_CHOICES,
        max_choices=2,
        null=True,
        blank=True,
    )

    main_pressures_effects = RichTextField( null=True, blank=True, 
        verbose_name= "2.3 Define main pressures / effects")

    main_source_effects = RichTextField( null=True, blank=True, 
        verbose_name= "2.4 Describe main sources of pressures / effects")
    
    main_environmental_responses = RichTextField( null=True, blank=True, 
        verbose_name= "2.5 Describe main environmental responses")

    main_environmental_responses = RichTextField( null=True, blank=True, 
        verbose_name= "2.5 Describe main environmental responses")

#2.6 Source / Pressure / Pathway / Receptor Relationships






#phase3
#phase4