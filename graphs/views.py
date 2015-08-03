import hashlib
import requests
import json
from flowspec.models import Route
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import get_object_or_404, render


def graphs(request, route_slug):
    start = request.GET.get('start')
    end = request.GET.get('end')
    route = get_object_or_404(Route, name=route_slug)
    h = hashlib.md5()
    h.update(route.junos_name)
    name_hash = h.hexdigest()
    # get the graphs (if any)
    if hasattr(settings, 'GRAPHS_API_URL'):
        if start and end:
            graphs = requests.get('%s%s/?start=%s&end=%s' % (settings.GRAPHS_API_URL, name_hash, start, end), verify=False)
        else:
            graphs = requests.get('%s%s/' % (settings.GRAPHS_API_URL, name_hash), verify=False)
    else:
        raise ImproperlyConfigured('You need to set GRAPHS_API_URL in settings.py')
    return render(
        request,
        'graphs/graphs.html',
        {'graphs_dict': json.loads(graphs.text)}
    )
