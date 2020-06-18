from rest_framework import serializers
from agents.models import Agent, Region, Persona


class AgentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Agent
        fields = ['url', 'id', 'first_name', 'last_name', 'first_time_agent', 'persona', 'region']
