from rest_framework import serializers
from agents.models import Agent


class AgentSerializer(serializers.ModelSerializer):
    persona = serializers.StringRelatedField()
    region = serializers.StringRelatedField()

    class Meta:
        model = Agent
        fields = ['url', 'id', 'first_name', 'last_name', 'first_time_agent', 'persona', 'region', ]
