from rest_framework import serializers
from .models import *

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields="__all__"