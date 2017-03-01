class DBSCAN(object):
#from sklearn.cluster import DBSCAN
import numpy as np
data = np.random.rand(500,3)

db = DBSCAN(eps=0.12, min_samples=1).fit(data)
labels = db.labels_
from collections import Counter
Counter(labels)

#def __init__(self, eps=0, min_points=2):
    #self.eps = eps
    #self.min_points = min_points
    #self.visited = []
    #self.noise = []
    #self.clusters = []
    #SSSSSself.dp = []

def cluster(self, data_points):
    self.visited = []
    self.dp = data_points
    c = 0
    for point in data_points:
        if point not in self.visited:
            self.visited.append(point)
            neighbours = self.region_query(point)
            if len(neighbours) < self.min_points:
                self.noise.append(point)
            else:
                c += 1
                self.expand_cluster(c, neighbours)

def expand_cluster(self, cluster_number, p_neighbours):
    cluster = ("Cluster: %d" % cluster_number, [])
    self.clusters.append(cluster)
    new_points = p_neighbours
    while new_points:
        new_points = self.pool(cluster, new_points)

def region_query(self, p):
    result = []
    for d in self.dp:
        distance = (((d[0] - p[0])**2 + (d[1] - p[1])**2 + (d[2] - p[2])**2)**0.5)
        if distance <= self.eps:
            result.append(d)
    return result

def pool(self, cluster, p_neighbours):
    new_neighbours = []
    for n in p_neighbours:
        if n not in self.visited:
            self.visited.append(n)
            n_neighbours = self.region_query(n)
            if len(n_neighbours) >= self.min_points:
                new_neighbours = self.unexplored(p_neighbours, n_neighbours)
        for c in self.clusters:
            if n not in c[1] and n not in cluster[1]:
                cluster[1].append(n)
    return new_neighbours

@staticmethod
def unexplored(x, y):
    z = []
    for p in y:
        if p not in x:
            z.append(p)
    return z


