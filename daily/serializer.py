from rest_framework import  serializers

from .models import  Runs,Leaderbord


class RunsListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Runs
        fields="__all__"

class RunsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Runs
        fields="__all__"


class LeaderbordListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Leaderbord
        fields=('seed','name','score')