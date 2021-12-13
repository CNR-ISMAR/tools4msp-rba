from django.conf.urls.static import static
from django.urls import include, path
from django.contrib import admin
from tools4msp_rba.settings import base, dev
from app import views
from rba import views

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from rba.views import CsList, CSDetailView

urlpatterns = [  
    path('django-admin/', admin.site.urls),
    path('admin/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('rba/list/', CsList.as_view()),
    path('rba/cs/<slug:slug>/', CSDetailView.as_view(), name='cs-view'),
    path('<filename>.html', views.html),
    path('', views.index),
    ] + static(base.STATIC_URL, document_root=base.STATIC_ROOT)



if dev.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),

    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]
