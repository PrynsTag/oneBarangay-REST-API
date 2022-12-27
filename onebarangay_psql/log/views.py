"""Views for Prometheus monitoring."""
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from prometheus_client import CONTENT_TYPE_LATEST

from onebarangay_psql.utils.prometheus import registry_to_text


@csrf_exempt
def prometheus_metrics(request):
    """Return the prometheus metrics as text."""
    return HttpResponse(registry_to_text(), content_type=CONTENT_TYPE_LATEST)
