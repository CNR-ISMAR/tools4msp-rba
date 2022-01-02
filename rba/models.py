from django.db import models
from django.db.models.fields.related import ManyToManyField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Orderable
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.core.fields import RichTextField
from multiselectfield import MultiSelectField
from rba import enumerations
from tools4msp.models import Pressure, Use, Env

#phase2
class CSphase2(ClusterableModel):
    title = models.CharField(max_length=400, blank=True, null=False)
    description = models.TextField( null=True, blank=True)

    condition_type = MultiSelectField(
        choices= enumerations.CONDITION_CHIOICE,
        max_choices=1,
        null=True,
        blank=True,
    )

    main_pressures_effects = models.TextField( null=True, blank=True, 
        verbose_name= "2.3 Define main pressures / effects")
    
    pressure_list = models.ManyToManyField(Pressure, through='Phase2Pressures', blank=True,
        verbose_name= "Pressures")
    

    main_source_effects = models.TextField( null=True, blank=True, 
        verbose_name= "2.4 Describe main sources of pressures / effects")
    
    use_list = models.ManyToManyField(Use, through='Phase2uses', blank=True,
        verbose_name= "Uses")
    
    main_environmental_responses = RichTextField( null=True, blank=True, 
        verbose_name= "2.5 Describe main environmental responses")
    
    env_list = models.ManyToManyField(Env, through='Phase2envs', blank=True,
        verbose_name= "Environmental Components")

    impact_chain = RichTextField( null=True, blank=True, 
        verbose_name= "2.6 Source / Pressure / Pathway / Receptor Relationships")
    
    def __str__(self):
        return self.title

# case study model and Phase 1
class CS(ClusterableModel): 
    title = models.CharField(max_length=400, blank=True, null=False)
    description = models.TextField ( null=True, blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    

    map_embed_url = models.CharField(max_length=600,blank=True, null=True)

    #phase1 
    study_area = models.TextField( null=True, blank=True, 
        verbose_name= "1.1 Define the Study Area")

    policy_objectives = models.TextField( null=True, blank=True, 
        verbose_name= "1.2 Define Policy objectives")
    

    ecosystem_services = models.TextField( null=True, blank=True, 
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

    future_scenarios = models.TextField( null=True, blank=True, 
        verbose_name= "1.4 Define future scenarios")
    
    phase2 = models.ManyToManyField(CSphase2, through='M2MPhase2', blank=True)


#phase3
#phase4

class M2MPhase2(models.Model): 
    phase_2 = models.ForeignKey(CSphase2, on_delete=models.CASCADE)
    phase_1 = models.ForeignKey(CS, on_delete=models.CASCADE) 

class Phase2Pressures(Orderable): 
    phase_2 = ParentalKey(CSphase2, related_name='phase2pressures_objects')
    pressure_list = models.ForeignKey(Pressure, on_delete=models.CASCADE)
    pressure_type = MultiSelectField(
        choices= enumerations.PRESSURE_TYPE_CHOICE,
        max_choices=1,
        null=True,
        blank=True,
    )
    pressure_description = RichTextField( null=True, blank=True, 
        verbose_name= "Description")
    layer = models.URLField(max_length=600,blank=True, null=True)
   

    def __str__(self):
        #return self.phase_2.title
        return self.pressure_list.label
  
class Phase2uses(Orderable): 
    phase_2 = ParentalKey(CSphase2, related_name='phase2uses_objects')
    use_list = models.ForeignKey(Use, on_delete=models.CASCADE)
    use_type = MultiSelectField(
        choices= enumerations.USE_TYPE_CHOICE,
        max_choices=1,
        null=True,
        blank=True,
    )
    use_description = RichTextField( null=True, blank=True, 
        verbose_name= "Description")
    layer = models.URLField(max_length=600,blank=True, null=True)


class Phase2envs(models.Model): 
    phase_2 = models.ForeignKey(CSphase2, on_delete=models.CASCADE)
    env_list = models.ForeignKey(Env, on_delete=models.CASCADE)

class PolicyObjectives(Orderable):
    phase_1 = ParentalKey(CS, related_name='polobj_objects')
    polobj = models.TextField ( null=True, blank=True,
        verbose_name= "Policy Objective")

class FutureScenarios(Orderable):
    phase_1 = ParentalKey(CS, related_name='futscen_objects')
    future_scen = models.TextField ( null=True, blank=True,
        verbose_name= "Future Scenarios")