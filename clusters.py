# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                                             		#
# 	A k-means clustering solver. There is am example problem included, which is commented out.	#
#                                                                                             		#
#	Author: Tyler Hooks                                                                       	#
#                                                                                             		#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


import math
import random
import re

def get_coordinates(coords):
	coordinates = []
	for coordinate in re.findall('\(\d\.*\d*,\s*\d\.*\d*\)', coords):
		coordinate = re.findall('\d\.*\d*', coordinate)
		coordinate_list = []
		for c in coordinate:
			coordinate_list.append(float(c))
		coordinates.append(tuple(coordinate_list))
	return coordinates
		

def get_centroids(coordinates, count):
	return random.sample(coordinates, count)

def get_distance(centroids, coordinate):
	distances = []
	for c in centroids:
		distance = math.sqrt(math.pow(c[0] - coordinate[0], 2) + math.pow(c[1] - coordinate[1], 2))
		distances.append(distance)
	return distances
	
def get_membership(centroids, coordinates):
	clusters = {}
	for c in range(len(centroids)):
		clusters[c] = []
	for coordinate in coordinates:
		distances = get_distance(centroids, coordinate)
		cluster = distances.index(min(distances))
		clusters[cluster].append(coordinate)
	return clusters

def get_new_centroids(clusters):
	new_centroids = []
	for cluster in clusters:
		x = []
		y = []
		for c in clusters[cluster]:
			x.append(c[0])
			y.append(c[1])
		new_centroid = (sum(x)/len(clusters[cluster]), sum(y)/len(clusters[cluster]))
		new_centroids.append(new_centroid)
	return new_centroids

try:
	coords = input("Please enter the coordinates: ")
	count = int(input("How many clusters do you wish to have? "))
	
	# Example problem. 
	# coords = "(1, 3), (3, 3) (4, 3), (5, 3) (1, 2), (4, 2), (1, 1) (2, 1)"
	# count = 2
	coordinates = get_coordinates(coords)
	centroids = get_centroids(coordinates, count)
	clusters = get_membership(centroids, coordinates)
	new_centroids = get_new_centroids(clusters)
	for iteration in range(5):
		if centroids == new_centroids or iteration == 4:
			for c in clusters:
				print(f"c{c}: {clusters[c]}")
			# print(f"Stopped on iteration {iteration + 1}.")
			break
		clusters = get_membership(centroids, coordinates)
		centroids = new_centroids
		new_centroids = get_new_centroids(clusters)
			
	
except Exception as e:
	print(f"Error: {e}")
