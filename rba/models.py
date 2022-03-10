from django.db import models
from django.db.models.fields.related import ManyToManyField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Orderable
from wagtail.core.models import Page
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.core.fields import RichTextField
from multiselectfield import MultiSelectField
from rba import enumerations
from tools4msp.models import Pressure, Use, Env
import numpy as np
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objs as go
import networkx as nx


#risk configuration
class CSphase2(ClusterableModel):
    title = models.CharField(max_length=400, blank=True, null=False)
    description = models.TextField( null=True, blank=True)

    condition_type = MultiSelectField(
        choices= enumerations.CONDITION_CHOICE,
        max_choices=1,
        null=True,
        blank=True,
    )

    main_pressures_effects = models.TextField( null=True, blank=True, 
        verbose_name= "Define main pressures / effects")
    
    pressure_list = models.ManyToManyField(Pressure, through='Phase2Pressures', blank=True,
        verbose_name= "Pressures")
    

    main_source_effects = models.TextField( null=True, blank=True, 
        verbose_name= "Describe main sources of pressures / effects")
    
    use_list = models.ManyToManyField(Use, through='Phase2uses', blank=True,
        verbose_name= "Uses")
    
    main_environmental_responses = models.TextField( null=True, blank=True, 
        verbose_name= "Describe main environmental receptors")
    
    env_list = models.ManyToManyField(Env, through='Phase2envs', blank=True,
        verbose_name= "Environmental Components")

    impact_chain = models.TextField( null=True, blank=True, 
        verbose_name= "Source / Pressure / Pathway / Receptor Relationships")
    
    def __str__(self):
        return self.title

    def _graph(self):
        phase = self
    
        up_data = [[up.use_list.label, up.pressure_list.label] for up in phase.pathup_objects.all()]
        pe_data = [[pe.pressure_list.label, pe.env_list.label, pe.env_list.label] for pe in phase.pathpe_objects.all()]
        data = []
        for up in  up_data:
            getted = False
            for pe in pe_data:
                if up[1] == pe[0]:
                    data.append([up[0], up[1], pe[1]])
                    getted = True
            if not getted:
                data.append([up[0], up[1], None])
                                    
        df = pd.DataFrame(data, columns=['Sources', 'Pressures', 'Receptors'])
        fig = px.parallel_categories(df,
                                     # color=df.index,
                                     dimensions=['Sources', 'Pressures', 'Receptors'],
                                     #layout=my_layout
        )
        fig.update_layout(showlegend=False)

        plt_div = plotly.offline.plot(fig, output_type='div')
        return plt_div

    def graph(self):
        phase = self
        up_edges = [[up.use_list.code, up.pressure_list.code] for up in phase.pathup_objects.all()]
        pe_edges = [[pe.pressure_list.code, pe.env_list.code] for pe in phase.pathpe_objects.all()]
        _u = [(up.use_list.code, up.use_list.label) for up in phase.pathup_objects.all()]
        _p1 = [(up.pressure_list.code, up.pressure_list.label) for up in phase.pathup_objects.all()]
        _p2 = [(pe.pressure_list.code, pe.pressure_list.label) for pe in phase.pathpe_objects.all()]
        _e = [(pe.env_list.code, pe.env_list.label) for pe in phase.pathpe_objects.all()]
        u_nodes = list(set(_u))
        p_nodes = list(set(_p1 + _p2))
        e_nodes = list(set(_e))

        pos = dict()
        pos.update( (node[0], (1, i)) for i, node in enumerate(u_nodes) ) # put nodes from X at x=1
        pos.update( (node[0], (2, i)) for i, node in enumerate(p_nodes) ) # put nodes from Y at x=2
        pos.update( (node[0], (3, i)) for i, node in enumerate(e_nodes) ) # put nodes from X at x=1

        edge_x = []
        edge_y = []
        for edge in up_edges + pe_edges:
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            edge_x.append(x0)
            edge_x.append(x1)
            edge_x.append(None)
            edge_y.append(y0)
            edge_y.append(y1)
            edge_y.append(None)

        edge_trace = go.Scatter(
            x=edge_x, y=edge_y,
            line=dict(width=0.5, color='#888'),
            hoverinfo='none',
            mode='lines')

        node_x = []
        node_y = []
        node_code = []
        node_label = []
        for node in u_nodes + p_nodes + e_nodes:
            x, y = pos[node[0]]
            node_x.append(x)
            node_y.append(y)
            node_code.append(node[0])
            node_label.append(node[1])
            
        node_trace = go.Scatter(
            x=node_x, y=node_y,
            text=node_code,
            customdata=np.expand_dims(node_label, axis=1),
            hovertemplate='<b>%{customdata[0]}</b>',
            mode='markers+text',
            textposition="top center",
            marker=dict(color='#000'),
            # hoverinfo='text',
            # marker=dict(
            #     # showscale=True,
            #     # colorscale options
            #     #'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
            #     #'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
            #                                 #'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
            #     colorscale='YlGnBu',
            #     reversescale=True,
            #     color=[],
            #     size=10,
            #     # colorbar=dict(
            #     #     thickness=15,
            #     #     title='Node Connections',
            #     #     xanchor='left',
            #     #     titleside='right'
            #     # ),
            #     line_width=2)
        )

        # Headers
        headers_y = max(node_y) + 1
        header_trace = go.Scatter(
            x=[1, 2, 3], y=[headers_y, headers_y, headers_y],
            text=['Sources', 'Pressures', 'Receptors'],
            # customdata=np.expand_dims(node_label, axis=1),
            # hovertemplate='<b>%{customdata[0]}</b>',
            mode='text',
            textposition="top center",
            textfont=dict(
                family="nunito",
                size=17,
                color="#4e73df",
            )
            
            # marker=dict(color='#000')
            # hoverinfo='text',
            # marker=dict(
            #     # showscale=True,
            #     # colorscale options
            #     #'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
            #     #'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
            #                                 #'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
            #     colorscale='YlGnBu',
            #     reversescale=True,
            #     color=[],
            #     size=10,
            #     # colorbar=dict(
            #     #     thickness=15,
            #     #     title='Node Connections',
            #     #     xanchor='left',
            #     #     titleside='right'
            #     # ),
            #     line_width=2)
        )

        config={
            'modeBarButtonsToRemove': ['zoom', 'pan', 'select', 'zoomIn', 'zoomOut', 'autoScale', 'resetScale', 'lasso2d', ],
            'displaylogo': False
        }
        fig = go.Figure(data=[edge_trace, node_trace, header_trace],
                        layout=go.Layout(
                            showlegend=False,
                            hovermode='closest',
                            margin=dict(b=20,l=5,r=5,t=40),
                            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                            paper_bgcolor='rgba(0,0,0,0)',
                            plot_bgcolor='rgba(0,0,0,0)'
                        ),
        )
        plt_div = plotly.offline.plot(fig, output_type='div', config=config)
        return plt_div

    mana_meas = models.TextField( null=True, blank=True, 
        verbose_name= "3.2 Define Management Measures")
    
    class Meta:
        verbose_name = 'Risk Configuration'
        verbose_name_plural = 'Risk Configurations'

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

    future_scenarios = models.TextField( null=True, blank=True, 
        verbose_name= "1.4 Define future scenarios")
    
    phase2 = models.ManyToManyField(CSphase2, through='M2MPhase2', blank=True)

    class Meta:
        verbose_name = 'Case Study'
        verbose_name_plural = 'Case Studies'


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
    data_source = models.URLField(max_length=600,blank=True, null=True)
    data_description = RichTextField( null=True, blank=True, 
        verbose_name= "Data Source description")
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
    data_source = models.URLField(max_length=600,blank=True, null=True)
    data_description = RichTextField( null=True, blank=True, 
        verbose_name= "Data Source description")
    layer = models.URLField(max_length=600,blank=True, null=True)


class Phase2envs(Orderable): 
    phase_2 = ParentalKey(CSphase2, related_name='phase2env_objects')
    env_list = models.ForeignKey(Env, on_delete=models.CASCADE)
    env_type = MultiSelectField(
        choices= enumerations.ENV_TYPE_CHOICE,
        max_choices=1,
        null=True,
        blank=True,
    )
    env_description = RichTextField( null=True, blank=True, 
        verbose_name= "Description")
    data_source = models.URLField(max_length=600,blank=True, null=True)
    data_description = RichTextField( null=True, blank=True, 
        verbose_name= "Data Source description")
    layer = models.URLField(max_length=600,blank=True, null=True)

class ManagementMeasures(Orderable):
    phase_2 = ParentalKey(CSphase2, related_name='mana_meas_objects')
    manameas = models.TextField ( null=True, blank=True,
        verbose_name= "Description Item")

class ManaMeas(Orderable):
    phase_2 = ParentalKey(CSphase2, related_name='manamea_objects')
    manamea = models.TextField ( null=True, blank=True,
        verbose_name= "Description Item")

class PolicyObjectives(Orderable):
    phase_1 = ParentalKey(CS, related_name='polobj_objects')
    polobj = models.TextField ( null=True, blank=True,
        verbose_name= "Policy Objective")
    polobj_desc = models.TextField ( null=True, blank=True,
        verbose_name= "Policy Objective Description")

class EcoService(Orderable):
    phase_1 = ParentalKey(CS, related_name='eco_objects')
    es_type = MultiSelectField(
        choices= enumerations.ES_TYPE_CHOICE,
        null=True,
        blank=True,
        verbose_name= "Section"
    )
    bio_type = MultiSelectField(
        choices= enumerations.BIO_TYPE_CHOICE,
        null=True,
        blank=True,
        verbose_name= "Section Type"
    )
    Title = models.TextField ( null=True, blank=True,
        verbose_name= "Ecosystem Service")
    
    es_description = RichTextField( null=True, blank=True, 
         verbose_name= "Ecosystem Service Description")

    

class FutureScenarios(Orderable):
    phase_1 = ParentalKey(CS, related_name='futscen_objects')
    future_scen = models.TextField ( null=True, blank=True,
        verbose_name= "Future Scenarios")
    future_scen_desc = models.TextField ( null=True, blank=True,
        verbose_name= "Scenario Description")

class Path_use_pres(Orderable):
    phase_2 = ParentalKey(CSphase2, related_name='pathup_objects')
    use_list = models.ForeignKey(Use, on_delete=models.CASCADE)
    pressure_list = models.ForeignKey(Pressure, on_delete=models.CASCADE)
    description = RichTextField( null=True, blank=True, 
        verbose_name= "Description")
    

class Path_pres_env(Orderable):
    phase_2 = ParentalKey(CSphase2, related_name='pathpe_objects')
    pressure_list = models.ForeignKey(Pressure, on_delete=models.CASCADE)
    env_list = models.ForeignKey(Env, on_delete=models.CASCADE)
    description = RichTextField( null=True, blank=True, 
        verbose_name= "Description")

class PolicyObjectives(Orderable):
    phase_1 = ParentalKey(CS, related_name='polobj_objects')
    polobj = models.TextField ( null=True, blank=True,
        verbose_name= "Policy Objective")
    polobj_desc = models.TextField ( null=True, blank=True,
        verbose_name= "Policy Objective Description")



# about risk base cea
class DocPage(Page):
    template = "rba/doc.html"
    doctitle = models.CharField(max_length=100, blank=False, null=True)
    docdesc = RichTextField( null=True, blank=True, 
        verbose_name= "description")
    content_panels = Page.content_panels + [
        FieldPanel("doctitle"),
        FieldPanel("docdesc"),
    ]
