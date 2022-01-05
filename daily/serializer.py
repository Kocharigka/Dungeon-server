from rest_framework import  serializers

from .models import  Runs,Leaderbord


class RunsListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Runs
        fields="__all__"

class RunsSeedSerializer(serializers.ModelSerializer):
    class Meta:
        model=Runs
        fields=["id","seed"]

class LeaderbordListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Leaderbord
        fields=('name','score')

class LeaderbordCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Leaderbord
        fields="__all__"
