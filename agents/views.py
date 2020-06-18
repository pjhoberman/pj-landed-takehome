from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from agents.models import Agent, Region, Persona
from agents.serializers import AgentSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'agents': reverse('agent-list', request=request, format=format),
    })


@api_view(['GET'])
def agent_list(request, format=None):
    """
    List all agents
    """
    if request.method == 'GET':
        agents = Agent.objects.all()
        serializer = AgentSerializer(agents, many=True, context={'request': request})
        return Response(serializer.data)


@api_view(['GET'])
def agent_detail(request, pk, format=None):
    """
    Return details on one agent
    """
    if request.method == "GET":
        try:
            agent = Agent.objects.get(pk=pk)
        except Agent.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = AgentSerializer(agent, context={'request': request})
        return Response(serializer.data)

