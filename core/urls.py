from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rate.urls', namespace='rate')),
    path('api/', include('api.urls', namespace='api'))
]

if 'survey' in settings.INSTALLED_APPS:
    urlpatterns += [
        url(r'^survey/', include('survey.urls'))
    ]
