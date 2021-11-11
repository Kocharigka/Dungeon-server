from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Runs
from .serializer import RunsListSerializer,LeaderbordListSerializer,RunsCreateSerializer

import datetime
# Create your views here.

class RunListView(APIView):
    def get(self,request):
        runs=Runs.objects
        serializer=RunsListSerializer(runs,many=True)
        return Response(serializer.data)

class RunDetailView(APIView):
    def get(self,request):
        runs=Runs.objects.filter(run_date=datetime.datetime.today())
        serializer=RunsListSerializer(runs,many=True)
        return Response(serializer.data)

class RunCreateView(APIView):
    def post(self,request):
        run=RunsCreateSerializer(data=request.data)
        if run.is_valid():
            run.save()
            return Response(status=201)
        else:
            return Response(status=203)