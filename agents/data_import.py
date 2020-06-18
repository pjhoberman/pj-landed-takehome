import json
from agents.models import Agent, Region, Persona

with open('data.json', 'r') as file:
    data = json.loads(file.read())

agents = data['agents']

for agent in agents:
    region, created = Region.objects.get_or_create(name=agent['region'])
    persona, created = Persona.objects.get_or_create(name=agent['persona'])
    agent['region'] = region
    agent['persona'] = persona
    Agent.objects.create(**agent)
