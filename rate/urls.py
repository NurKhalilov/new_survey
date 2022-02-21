from django.urls import path
from . import views

app_name = 'rate'

urlpatterns = [
    # path('', views.dashboard, name='dashboard'),
    path('report/<uuid:pk>/', views.report_add, name='report_add'),
    path('json/', views.json, name='json'),
    # path('survey-analysis/', views.survey, name='survey-analysis'),
    path('graph/', views.graph_show, name='graph_show'),
]

