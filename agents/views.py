# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from agents.models import Agent, Region, Persona
from agents.serializers import AgentSerializer


@csrf_exempt
def agent_list(request):
    """
    List all agents
    """
    if request.method == 'GET':
        agents = Agent.objects.all()
        serializer = AgentSerializer(agents, many=True)
        return JsonResponse(serializer.data, safe=False)


def agent_detail(request, pk):
    """
    Return details on one agent
    """
    if request.method == "GET":
        try:
            agent = Agent.objects.get(pk=pk)
        except Agent.DoesNotExist:
            return HttpResponse(status=404)
        serializer = AgentSerializer(agent)
        return JsonResponse(serializer.data)

