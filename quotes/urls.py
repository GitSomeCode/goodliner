from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from quotes import views

urlpatterns = patterns("",

	url(r"^$", views.randomQuote),
	url(r"(?P<qHash>[a-f0-9]{3})$", views.getQuote),
	url(r"inc$", views.incrementQuote),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)