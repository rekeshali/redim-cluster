#### PCA Stuff ####
def svd(db):
    from tools import buildX
    from scipy import linalg as la
    X = buildX(db)
    [U,S,Vh] = la.svd(X)
    return U,S,Vh

def reduct(U,S,Vh,k):
    import numpy as np
    from tools import diag
    Sk  = S[0:k]
    Uk  = U[:,0:k]
    Vhk = Vh[0:k,:]
    Sig = diag(Sk)
    X = Uk*Sig*Vhk
    return X

#### Clustering ####
def kmeans(k,X):
    import numpy as np
    key = list(map(str,range(k)))
#     Mmean = np.zeros((k,X.shape[1]))
    iters = 1
    for it in range(iters):
#         M = init_means(k,X) # randomly assign clusters to k instances
        M = X[list(range(k)),:]
        C = update_cluster(key,X,M) # assign clusters to nearest neighbors
        Cold = 0 # condition to break while
        i = 0
        while Cold != C: # breaks if clusters don't change
            Cold = C.copy()
            M = update_means(key,X,M,C) # recalculates cluster means
            C = update_cluster(key,X,M)
            i += 1
#         Mmean = Mmean + M
#     Mmean = Mmean/iters
#     C = update_cluster(key,X,Mmean)
    return C,i

def init_means(k,X):
    import random
    import numpy as np
    ninst = len(X[:,0])
    randidx = list(range(ninst))
    random.shuffle(randidx)
    M = X[randidx[0],:]
    for idx in randidx[1:k]:
        M = np.vstack((M,X[idx,:]))
    return M

def update_cluster(key,X,M):
    import numpy as np
    C = {}
    for tooth in key:
        C[tooth] = []

    for n,row in enumerate(X): # for all instances
        min_dist = float('inf')
        for m,row_mean in enumerate(M): # check against mean of every cluster
            dist = np.sqrt(np.sum(np.square(row - row_mean))) # euclidean norm
            if dist < min_dist:
                min_dist = dist
                clust = m
        C[str(clust)].append(n)
    return C

def update_means(key,X,M,C):
    import numpy as np
    nfeat = M.shape[1]
    for c,tooth in enumerate(key):
        for n in range(nfeat):
            M[c,n] = np.mean(X[C[tooth],n])
    return M
