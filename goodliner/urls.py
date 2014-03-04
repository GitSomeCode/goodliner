from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'goodliner.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r"^", include("quotes.urls")),
    url(r"^q/", include("quotes.urls")),
    #url(r"^about/$", direct_to_template, {"template": "goodliner/about.html"}),
    url(r"^about/$", TemplateView.as_view(template_name = "goodliner/about.html")),

    url(r'^admin/', include(admin.site.urls)),
)

	




	
