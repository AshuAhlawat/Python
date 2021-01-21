from django.shortcuts import render
from django.http import response, HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

from .models import Note
from .serializers import NoteSerializer

from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# @crsf_excempt

def home(request):
    
    if request.method == 'GET':
        notes=Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method =='POST':
        data = JSONParser().parse(request)
        serializer = NoteSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)