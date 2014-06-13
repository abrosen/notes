#basic kmeans algorithm

import math
# metric distance
# this is what we want to minimize
# using euclidean norm squared, but it could be anythign
def distance(point, centroid):
    return math.sqrt(sum(map( lambda x, y: (x-y)**2, point, centroid)  ))**2


def bootstrap():
    pass

def assignment(points, centroids):
    for point in points:
        closest = float("+inf")
        for centroid in centroids.keys():
            if distance(point, centroid) < closest:
                closest = centroid
        centroid[closest].append(point)
    return centroids

def update(centroids):




