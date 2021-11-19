from rest_framework.serializers import ModelSerializer

from .models import *

class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class JoinedMemberSerializer(ModelSerializer):
    class Meta:
        model = JoinedMember
        fields = '__all__'