from rest_framework import  serializers

from .models import  Runs,Leaderbord,GameSave


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
        fields=('name','score')

class LeaderbordCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Leaderbord
        fields="__all__"

class SaveSerializer(serializers.ModelSerializer):
    class Meta:
        model=GameSave
        fields="__all"
