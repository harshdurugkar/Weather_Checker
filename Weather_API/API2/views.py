from django.shortcuts import render
from django.http import HttpResponse
import os
import urllib.request
import json
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import numpy as np
from plotly.offline import plot
import plotly.graph_objs as go
from django.views.generic import TemplateView


def index(request):
    try:
        if request.method == 'POST':
            city = request.POST['city']
            source = urllib.request.urlopen(
                'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=173647a11ec04831b5779e4e83b64827').read()
            list_of_data = json.loads(source)
            source1 = urllib.request.urlopen(
                'https://timezone.abstractapi.com/v1/current_time/?api_key=87a9cfeccfa0489fb6c82f1f2c0f2a3f&location='+city).read()
            list_of_data1 = json.loads(source1)
            data = {
                "country_code": str(list_of_data['sys']['country']),
                "coordinate": str(list_of_data['coord']['lon']) + ' , ' + str(list_of_data['coord']['lat']),
                "temp": str(list_of_data['main']['temp']) + ' °C',
                "pressure": str(list_of_data['main']['pressure']),
                "humidity": str(list_of_data['main']['humidity']),
                "main": str(list_of_data['weather'][0]['main']),
                "description": str(list_of_data['weather'][0]['description']),
                "icon": str(list_of_data['weather'][0]['icon']),
                "city_name": str(list_of_data['name']),
                "curt": str(list_of_data1['datetime']),
                "tl": str(list_of_data1['timezone_location']),
            }
            print(data)
        else:
            data = {}
        return render(request, 'API2/api.html', data)
    except:
        return render(request, 'sorry.html')


#         context = super(Graph, self).get_context_data(**kwargs)
#
#         x = [-2,0,4,6,7]
#         y = [q**2-q+3 for q in x]
#         trace1 = go.Scatter(x=x, y=y, marker={'color': 'red', 'symbol': 104, 'size': "10"},
#                             mode="lines",  name='1st Trace')
#
#         data=go.Data([trace1])
#         layout=go.Layout(title="Meine Daten", xaxis={'title':'x1'}, yaxis={'title':'x2'})
#         figure=go.Figure(data=data,layout=layout)
#         div = opy.plot(figure, auto_open=False, output_type='div')
#
#         context['graph'] = div
#
#         return context


                                 # For Plotting a graph method 2
# def home(request):
#     def scatter():
#         x1 = [1,2,3,4]
#         y1 = [30, 35, 25, 45]
#         trace = go.Scatter(
#             x=x1,
#             y = y1
#         )
#         layout = dict(
#             title='Simple Graph',
#             xaxis=dict(range=[min(x1), max(x1)]),
#             yaxis = dict(range=[min(y1), max(y1)])
#         )
#
#         fig = go.Figure(data=[trace], layout=layout)
#         plot_div = plot(fig, output_type='div', include_plotlyjs=False)
#         return plot_div
#
#     context ={
#         'plot1': scatter()
#     }
#     return render(request, 'API2/api.html', context)


