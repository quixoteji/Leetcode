import numpy as np

def run_k_means(X, initial_centroids, max_iters) :
    m, n = X.shape
    k = initial_centroids.shape[0]
    idx = np.zeros(m)
    centroids = initial_centroids
    
    for _ in range(max_iters):
        idx = find_closest_centroids(X, centroids)
        centroids = compute_centroids(X, idx, k)
    
    return idx, centroids

def find_closest_centroids(X, centroids):
    m = X.shape[0]
    k = centroids.shape[0] 
    idx = np.zeros(m)  
    
    for i in range(m):
        min_dist = float('inf')  
        for j in range(k):
            dist = np.sum((X[i,:] - centroids[j,:]) ** 2) 
            if dist < min_dist:
                min_dist = dist
                idx[i] = j
    return idx

def compute_centroids(X, idx, k):
    m, n = X.shape
    centroids = np.zeros((k, n))
    
    for i in range(k):
        indices = np.where(idx == i)
        centroids[i,:] = (np.sum(X[indices,:], axis=1) / len(indices[0])).ravel()