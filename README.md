# Flowspy Graphs
A flowspy plugin which can retrieve graphs for flowspec rules and present
them along with the applied rules.


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
Here we are going to demonstrate how our graphs api was created.


