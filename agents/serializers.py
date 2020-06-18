from rest_framework import serializers
from agents.models import Agent, Region, Persona


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['id', 'first_name', 'last_name', 'first_time_agent', 'persona', 'region']
