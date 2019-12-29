from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
#import sys
#sys.path.insert(0, '/Users/0220182218/Desktop/Total\ Sky\ Imager/processing/')
import classprocess
# Create your views here.
@api_view(["POST"])
def latestcc(heightdata):
    camera.capture('/home/pi/Desktop/image.jpg')
    cloudcover=classprocess.Process('/home/pi/Desktop/image.jpg')
    cloudcover=str(cloudcover.calccover)
    return JsonResponse("The latest cloud coverage is:"+cloudcover+" %",safe=False)
