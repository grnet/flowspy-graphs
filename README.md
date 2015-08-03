# Flowspy Graphs
A flowspy plugin which can retrieve graphs for flowspec rules and present
them along with the applied rules.

Works with flowspy v1.3


## Installation
- `pip install https://github.com/grnet/flowspy-graphs`

- Add `graphs` in installed apps

- Add GRAPHS_API_URL in flowspy's setting file in order to point to your
graphs api.

- in the bottom of flowspy/urls.py:

	from graphs import urls as graphs_urls

	urlpatterns += patterns(''
		url(r'^graphs/', include(graphs.urls)),
	)


## Creating the graphs api
Here we are going to demonstrate how our graphs api was created:
In GRNET, we store stats collected via snmp from the network devices into rrd files,
which are being discovered and stored from a script. Then their name (based on)
the `junos_name` of the rule in flowspy is hashed into an md5 hash. Then we have
the following urls:

	url(r'^$', views.list_graphs, name='all_graphs'),
    url(r'^(?P<graph_hash>\w+)/(?P<hostname>\w+)/(?P<graph_type>\w+)/$', views.list_graphs, name='graphs_type'),
    url(r'^(?P<graph_hash>\w+)/(?P<hostname>\w+)/$', views.list_graphs, name='host_graphs'),
    url(r'^(?P<graph_hash>\w+)/$', views.list_graphs, name='graphs'),

in order to serve each graph. The response has the following format:

	{'graphs': [{"type": "bytes", "host": "kolettir.grnet.gr", "hash": "51a8c1d06bb59a0a6aaf4983f04a35b7", "img": "<IMAGE_AS_BASE_64>"}]}

