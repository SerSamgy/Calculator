from django.shortcuts import render
from models import Solver

def root(request):
    solver = Solver()
    context = {'solver': solver}
    return render(request, 'calculator/index.html', context)