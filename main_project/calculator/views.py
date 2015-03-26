from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from serializers import SolverSerializer
from models import Solver
from rest_framework.renderers import JSONRenderer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

def root(request):
    return render(request, 'calculator/index.html')

@csrf_exempt
@require_GET
def get_result(request, format=None):
    try:
        solver = Solver.objects.get(pk=0)
    except Solver.DoesNotExist:
        solver = Solver.objects.create(pk=0)

    serializer = SolverSerializer(solver)
    return JSONResponse(serializer.data)

# RE: ^\d+(?:.\d+)?[\/\+\-\*]\d+(?:.\d+)?$
@csrf_exempt
@require_POST
@api_view(['POST'])
def set_expression(request, format=None):
    try:
        solver = Solver.objects.get(pk=0)
    except Solver.DoesNotExist:
        solver = Solver.objects.create(pk=0)

    data = JSONParser().parse(request)
    serializer = SolverSerializer(solver, data=data)
    if serializer.is_valid():
        serializer.save()
        return JSONResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JSONResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)