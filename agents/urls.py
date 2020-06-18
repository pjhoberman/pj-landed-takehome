from django.urls import path
from django.views.generic import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns
from agents import views

urlpatterns = [
    path('', views.api_root),
    path('agent/', views.agent_list, name="agent-list"),
    path('agent/<int:pk>', views.agent_detail, name="agent-detail"),

    path('swagger-ui', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name="swagger-ui")
]

urlpatterns = format_suffix_patterns(urlpatterns)
