from django.shortcuts import render
from django.shortcuts import HttpResponse
import random

def index(request):
    # randomlistx1 = random.sample(range(1, 10), 5)
    # randomlistx2 = random.sample(range(1, 10), 5)
    randomlistx1 = [1, 2, 3, 4, 5]
    randomlistx2 = [1, 2, 3, 4, 5]
    randomlisty1 = random.sample(range(10, 30), 5)
    randomlisty2 = random.sample(range(10, 30), 5)
    data = {'x1': randomlistx1,
            'x2': randomlistx2,
            'y1': randomlisty1,
            'y2': randomlisty2,
            }
    return render(request, 'plot_graph/index.html', data)


