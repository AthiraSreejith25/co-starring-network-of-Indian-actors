#this module contains functions that help create a graph with a certain theme.

import networkx as nx
from itertools import combinations


#this function makes the nodes of the graph
def make_nodes(data, years, graph):

	actors = set()

	for i in data[1:]:

		if i[1] != '':

			if int(i[1][1:-1]) in years:

				actors.update(i[-3:])

	actors.remove('')

	graph.add_nodes_from(actors, color = "#03DAC6")


#helps to make the graph weighted
def edge_weight(node_1, node_2, graph):

	info =  graph.get_edge_data(node_1, node_2)

	if info == None:

		return 0

	else:

		return info['weight']


#this function makes the edgess of the graph
def make_edges(data, years, graph):

	for i in data[1:]:

		if i[1] != '':

			#i[1] is basically the year in the csv data and [1:-1] removes unwanted start and end characters of the string
			if int(i[1][1:-1]) in years:

				affiliates = i[-3:]

				if '' not in affiliates:

					co_stars = list(combinations(affiliates, 2))

					#weight is checked using edge_weight function and updated += 1
					graph.add_edge(co_stars[0][0], co_stars[0][1], weight = edge_weight(co_stars[0][0], co_stars[0][1], graph) + 1, color = "#018786")
					graph.add_edge(co_stars[1][0], co_stars[1][1], weight = edge_weight(co_stars[1][0], co_stars[1][1], graph) + 1, color = "#018786")

				elif affiliates.count('') == 1:

					affiliates.remove('')
					graph.add_edge(affiliates[0], affiliates[1], weight = edge_weight(affiliates[0], affiliates[1], graph) + 1, color = "#018786")


#puts all the functions together to make the create_graph function which makes graph for a given time period
def create_graph(data, from_year=1950, till_year=2022):

	G = nx.Graph()
	years = list(range(from_year, till_year+1))

	make_nodes(data, years, G)
	make_edges(data, years, G)

	return G
