def buildX(db):
    import numpy as np
    from explore import key
    X = np.asmatrix(db[key[0]]).T
    for tooth in key[1:]:
        col = np.asmatrix(db[tooth]).T
        X = np.hstack((X,col))
    return X

def svd(db):
    from scipy import linalg as la
    X = buildX(db)
    [U,S,Vh] = la.svd(X)
    return U,S,Vh

def diag(S):
    import numpy as np
    rank = len(S)
    Sig = [[0 for x in range(rank)] for y in range(rank)]
    for i in range(rank):
        Sig[i][i] = S[i]
    return np.asmatrix(Sig)

def reduct(U,S,Vh,k):
    import numpy as np
    Sk  = S[0:k]
    Uk  = U[:,0:k]
    Vhk = Vh[0:k,:]
    Sig = diag(Sk)
    X = Uk*Sig*Vhk
    return X
