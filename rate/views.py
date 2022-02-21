from django.shortcuts import render, get_object_or_404, redirect, reverse
from .forms import RateAddForm
from .utils import json_maker, get_plot
import pandas as pd
from .models import Region

#
# def dashboard(request):
#     regions = Region.objects.all()
#     return render(request,
#                   'account/dashboard.html',
#                   {'section': 'dashboard',
#                    'regions': regions})


def report_add(request, pk):
    form = RateAddForm(region_id=pk)
    if request.method == 'POST':
        form = RateAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/survey/2/')
        else:
            print("Something went wrong!")
            form = RateAddForm(request.POST, region_id=pk)
    return render(request,
                  'account/report.html',
                  {'form': form})
    

def json(request):
    data = json_maker()
    return render(request,
                  'report/report.html',
                  {'data': data})

# def survey(request):
#     data = survey_json()
#     return render(request,
#                   'report/survey-res.html',
#                   {'data': data})


def graph_show(request):
    chart = get_plot()
    return render(request,
                  'report/graph.html',
                  {'chart': chart})
    