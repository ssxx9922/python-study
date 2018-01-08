from django.shortcuts import render
from django.http import HttpResponse
import json


def list(request):
    resp = {'errorcode': 100, 'detail': 'Get success'}
    return HttpResponse(json.dumps(resp), content_type="application/json")

def details(request):
    return HttpResponse('details')

def write(request):
    return HttpResponse('write')

def delete(request):
    return HttpResponse('delete')