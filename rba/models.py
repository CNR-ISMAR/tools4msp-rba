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

    #phase2

    

    #phase3

    #phase4


  
