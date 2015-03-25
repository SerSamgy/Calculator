from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt
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
def get_result(request):
    try:
        solver = Solver.objects.get(pk=0)
    except Solver.DoesNotExist:
        solver = Solver.objects.create(pk=0)

    if request.method == 'GET':
        serializer = SolverSerializer(solver)
        return JSONResponse(serializer.data)