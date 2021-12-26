from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Runs,Leaderbord,GameSave
from .serializer import RunsSeedSerializer,RunsListSerializer,LeaderbordListSerializer,RunsCreateSerializer,LeaderbordCreateSerializer,SaveSerializer

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
        serializer=RunsSeedSerializer(runs,many=True)
        return Response(serializer.data)

class RunCreateView(APIView):
    def post(self,request):
        run=RunsCreateSerializer(data=request.data)
        if run.is_valid():
            run.save()
            return Response(status=201)
        else:
            return Response(status=203)

class LeaderbordListView(APIView):
    def JsonToOk(self,data):
        return {"seed":int(data['seed']),
                "name":data['name'],
                "score":int(data["score"])}
    def get(self,request):
        today_seed=Runs.objects.filter(run_date=datetime.datetime.today())
        board=Leaderbord.objects.filter(seed=today_seed[0]).order_by('-score')[:10]
        serializer=LeaderbordListSerializer(board,many=True)
        return Response(serializer.data)

    def post(self,request):
        record=LeaderbordCreateSerializer(data=self.JsonToOk(request.data))
        if record.is_valid():
            record.save()
            return Response(status=201)
        else:
            return Response(status=203)

class SaveView(APIView):
    def get(self,request):
        saves=GameSave.objects
        serializer=LeaderbordListSerializer(saves,many=True)
        return Response(serializer.data)

    def post(self,request):
        record=SaveSerializer(data=request.data)
        if record.is_valid():
            record.save()
            return Response(status=201)
        else:
            return Response(status=203)

