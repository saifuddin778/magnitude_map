from __future__ import division
import math
import random
from functions import Functions

funcs_ = Functions()
__author__ = 'Saifuddin Abdullah'

"""
Magnitude Mapping - A simple way to generate magnitude based clusters of a set of vectors.
"""
class magnitude_map(object):
    def __init__(self, data):
        self.data = data
        self.dimension = len(data[0][:-1])
        self.centroid = self.find_mean_center()
        self.create_map()
        
    def mag(self, v):
        return math.sqrt(sum([math.pow(a, 2) for a in v]))

    def dot(self, v1, v2):
        return sum([a*b for a,b in zip(v1, v2)])

    def mean(self, v):
        return sum(v)/len(v)
    
    def angle(self, v1, v2):
        dot_ = self.dot(v1, v2)
        mag_prod = self.mag(v1)*self.mag(v2)
        final = dot_/mag_prod
        try:
            return math.acos(final)
        except:
            return -1

    def find_mean_center(self):
        centroid = []
        t = zip(*self.data)
        for a in xrange(0, len(t)-1):
            centroid.append(self.mean(t[a]))
        return centroid           

    def ones_(self):
        return [1 for _ in xrange(0, self.dimension)]

    def flatten(self, item, y):
        for a in item:
            if type(a) == type([]):
                self.flatten(a, y)
            else:
                y.append(a)
        return y
    
    def create_map(self):
        self.h = {}
        for i in xrange(0, len(self.data)):
            point = self.data[i]
            
            mag_ = self.mag(point)
            if self.h.has_key(mag_):
                self.h[mag_].append((i, self.angle(self.centroid, point)))
            else:
                self.h[mag_] = []
                self.h[mag_].append((i, self.angle(self.centroid, point)))
            

    def distance(self, v1, v2):
        return math.sqrt(sum([math.pow(a-b, 2) for a,b in zip(v1, v2)]))
    
    def query(self, v):
        mag_ = self.mag(v)
        angle_ = self.angle(self.centroid, v)
        closest_mags = sorted(self.h.keys(), key=lambda n: abs(n-mag_))[0:self.dimension]
        closest_angles = self.flatten(map(lambda n: self.h[n], closest_mags), [])
        closest_angles = sorted(closest_angles, key=lambda n: abs(n[1] - angle_))
        return {'closest_items': map(lambda n: n[0], closest_angles)}

    def get_cluster(self, value):
        key = sorted(self.h.keys(), key=lambda n: abs(n-value))[0]
        return {'key': key, 'cluster_members': map(lambda q: q[0], self.h[key])}

    def find_cluster(self, v):
        mag_ = self.mag(v)
        most_probable = sorted(self.h.keys(), key=lambda n: abs(n-mag_))[0]
        return {'key': most_probable, 'cluster_members': map(lambda n: n[0], self.h[most_probable])}
