#this module has the main functions that will deal with calculating the attributes over time

from constructor import *
import numpy as np
import csv

#this function calculates the desired attribute by gradually moving through the years. Example: 1950-55, 1951-56, 1952-57 ...
def moving_scan(data, attribute, window, start=1950, end=2022):

	y = []

	for year in range(start, end-window+2):

		G = create_graph(data, year, year+window-1)

		print('calculating desired attribute: {} for year {} to {}'.format(attribute, year, year + window))

		if attribute == 'nodes':

			y.append(G.number_of_nodes())

		elif attribute == 'degrees':

			degrees = [G.degree(i) for i in G.nodes]
			y.append(np.unique(degrees, return_counts=True))

		elif attribute == 'degree_centrality':

			y.append(nx.degree_centrality(G))

		elif attribute == 'closeness_centrality':

			y.append(nx.closeness_centrality(G))

		elif attribute == 'betweenness_centrality':

			y.append(nx.betweenness_centrality(G))

		elif attribute == 'eigenvector_centrality':

			y.append(nx.eigenvector_centrality(G))

		elif attribute == 'density':

			m = G.number_of_edges()
			n = G.number_of_nodes()

			y.append(2*m/(n*(n-1)))

	return y

#this function calculates the desired attribute by moving through discrete class intervals. Example: 1950-55, 1955-60, 1965-70 ...
def interval_scan(data, attribute, window, start=1950, end=2022):

	y = []
	n = 0

	year = start + n * window


	while year < end:

		G = create_graph(data, year, year + window)

		print('calculating desired attribute: {} for year {} to {}'.format(attribute, year, year + window))

		if attribute == 'nodes':

			y.append(G.number_of_nodes())

		elif attribute == 'degrees':

			degrees = [G.degree(i) for i in G.nodes]
			y.append(np.unique(degrees, return_counts=True))

		elif attribute == 'degree_centrality':

			y.append(nx.degree_centrality(G))

		elif attribute == 'closeness_centrality':

			y.append(nx.closeness_centrality(G))

		elif attribute == 'betweenness_centrality':

			y.append(nx.betweenness_centrality(G))

		elif attribute == 'eigenvector_centrality':

			y.append(nx.eigenvector_centrality(G))

		elif attribute == 'density':

			m = G.number_of_edges()
			n = G.number_of_nodes()

			y.append(2*m/(n*(n-1)))

		n += 1
		year = start + n * window

	return y


#returns list of top n (for desired attribute) for every year
def top_n(_list, top=10):

	m = []

	print('Making a list of top {} for every year...'.format(str(top)))

	for i in _list:

		top_list = sorted([(v, k) for k, v in i.items()], reverse=True)[:top]
		m.append([(round(i[0],4), i[1]) for i in top_list])

	return m


#dumps the top_n out list to csv file
def dump_2_csv(_list, file):

	with open(file, 'w') as f:

		write = csv.writer(f)

		for i in _list:
			for j in i:

				write.writerow([j[1], j[0]])

			write.writerow(['', ''])

	print('Successfully dumped to {}'.format(file))
