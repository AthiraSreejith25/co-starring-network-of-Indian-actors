#!/usr/bin/python3

from constructor import *
from visual import *
from analyse import *

import csv
import matplotlib.pyplot as plt
import numpy as np

#Loads the data set
with open('movies_data.csv', 'r', encoding='ISO-8859-1') as file:

        movie_dataset = list(csv.reader(file))


#Degree distribution

#----all-years

G = create_graph(movie_dataset)

degrees = [G.degree(i) for i in G.nodes]
deg_dist = np.unique(degrees, return_counts=True)
plt.plot(deg_dist[0], deg_dist[1], 'ro-')

plt.ylabel('frequency')
plt.xlabel('degree')
plt.grid(True)
plt.title('Degree distribution (1950-2022)')
plt.savefig('deg_dist_all_years.png')
#plt.show()


#----year-wise

degs = interval_scan(movie_dataset, 'degrees', 10)

for i in range(len(degs)):

	deg_dist = np.unique(degs[i], return_counts=True)

	#to avoid log(0) since it is undefined, we remove elements with freq = 0
	for j in range(len(deg_dist[1])):

		if deg_dist[1][j] == 0:

			del(deg_dist[1][j])
			del(deg_dist[0][j])


	plt.bar(np.log(deg_dist[0][1:]), np.log(deg_dist[1][1:]))

	plt.ylabel('log(frequency)')
	plt.xlabel('log(degree)')
	plt.grid(True)
	plt.title('Degree distribution log-log ({}-{})'.format(str(1950+10*i), str(1950+10*(i+1))))
	plt.savefig('deg_dist_{}.png'.format(str(1950+10*i)))
	plt.show()



#Network size

net_size = moving_scan(movie_dataset, 'nodes', 3)

plt.plot(range(1950,2021), net_size)
plt.ylabel('number of actors (3 year total)')
plt.xlabel('year')
plt.grid(True)
plt.title('Network Size')
plt.savefig('network_size.png')
#plt.show()


#Network density

net_density = moving_scan(movie_dataset, 'density', 3)

plt.plot(range(1950,2021), net_density)
plt.ylabel('density (for 3 years)')
plt.xlabel('year')
plt.grid(True)
plt.title('Network Density')
plt.savefig('network_density.png')
#plt.show()


#Centralities

deg_cen = interval_scan(movie_dataset, 'degree_centrality', 5)
btw_cen = interval_scan(movie_dataset, 'betweenness_centrality', 5)
cls_cen = interval_scan(movie_dataset, 'closeness_centrality', 5)
eig_cen = interval_scan(movie_dataset, 'eigenvector_centrality', 5)

dump_2_csv(top_n(deg_cen), 'deg_cen.csv')
dump_2_csv(top_n(btw_cen), 'btw_cen.csv')
dump_2_csv(top_n(cls_cen), 'cls_cen.csv')
dump_2_csv(top_n(eig_cen), 'eig_cen.csv')


#Visuals (pandemic and pre-pandemic)

#2018 and 2019
pre_pandemic = create_graph(movie_dataset, 2018, 2019)
display(pre_pandemic, 'pre_pandemic.html')

#2020 and 2021
pandemic = create_graph(movie_dataset, 2020, 2021)
display(pandemic, 'pandemic.html')

