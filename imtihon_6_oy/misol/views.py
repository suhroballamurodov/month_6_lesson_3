from django.shortcuts import render
from .models import *


def math(request):
    maths = MatheModel.objects.all()
    tests = TestModel.objects.all()
    return render(request, 'math.html', {'maths': maths, 'tests':tests})

def test(request):
    maths = MatheModel.objects.all()
    tests = TestModel.objects.all()
    return render(request, 'test.html', {'maths': maths, 'tests':tests})