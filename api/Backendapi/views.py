from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from TSIapi.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

# from django.shortcuts import render
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from django.http import JsonResponse
# from django.core import serializers
# from django.conf import settings
# import json
# # Create your views here.
# @api_view(["POST"])
# #def CloudCover(imagejson):
#    # image=json.loads(imagejson.body)
#
# # def IdealWeight(heightdata):
# #     try:
# #         height=json.loads(heightdata.body)
# #         weight=str(height*10)
# #         return JsonResponse("Ideal weight should be:"+weight+" kg",safe=False)
# #     except ValueError as e:
# #         return Response(e.args[0],status.HTTP_400_BAD_REQUEST)