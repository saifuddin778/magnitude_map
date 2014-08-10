magnitude_map
=============

This is an experiment over the concept of LSH, in which a dataset elements can be hashed based on their magnitudes, and further can be queried with the similarity of their angle from the dataset's centroid. 

####Basic Usage:
````python
>>> from magnitude_map import magnitude_map
>>> data = [[1,2,3,4], [5,6,7,8], [9,10,11,12]...]
>>> map_ = magnitude_map(data)
>>> map_.query([1,2,3,4])
>>> {'closest_items': [indices of closest items]}
```
####Other functionalities:
* You can obtain the most probable cluster for any given data input using:
```python
>>> map_.find_cluster([1,2,3,4])
>>> {'key': clusters_magnitude_identity, 'cluster_members': [indices of vectors in this cluster]}
```
* You can also get the most probable cluster for a given magnitude or any numerical value as well:
```python
>>> map_.get_cluster(0.023)
>>> {'key': 0.024, 'cluster_members': [indices of vectors in this cluster]}
```
