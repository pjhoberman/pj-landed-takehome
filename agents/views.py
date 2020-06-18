from django.db.models import Q

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
    List all agents, or add query paramaters to filter
    Filtering is an OR query, so if you filter on two regions and a name,
    it's the same as saying "Agent is in region 1 OR region 2 OR their first name is Rob"

    All variable text fields are case insensitive and look for your text in the field's text.
    So, these searches will all return Robert: "rob", "Rob", "ober", "Robert"

    Filterable by the following:
        first_name (variable text)
        last_name (variable text)
        first_time_agent (bool)
        region (multi-select)
        personas (multi-select)

    """
    if request.method == 'GET':
        agents = Agent.objects.all()
        q = Q()
        # todo: and vs or, on a field or between fields
        for param, value in request.query_params.lists():
            if param in ['region', 'persona']:
                for val in value:
                    q |= Q(**{'%s__name__icontains' % param: val})

            elif param in ['first_name', 'last_name']:
                for val in value:
                    q |= Q(**{'%s__icontains' % param: val})

            elif param == 'first_time_agent':
                val = any([True if val.lower() in ["true", "1", "yes"] else False for val in value])
                q |= Q(first_time_agent=val)

        agents = agents.filter(q)
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

