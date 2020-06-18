from django.urls import path
from agents import views

urlpatterns = [
    path('agent/', views.agent_list, name="agent_list"),
    path('agent/<int:pk>', views.agent_detail, name="agent_detail"),
]