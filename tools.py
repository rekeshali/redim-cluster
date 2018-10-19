#!/usr/bin/python
# build a matrix from dict
def buildX(db):
    import numpy as np
    from explore import key
    X = np.asmatrix(db[key[0]]).T
    for tooth in key[1:]:
        col = np.asmatrix(db[tooth]).T
        X = np.hstack((X,col))
    return X

# returns array containing percent variance as where index = #eigenvalues
def percent_var(S):
    import numpy as np
    S2 = pow(S,2)
    sumS = sum(S2)
    PV = [S2[0]]
    k = []
    for val in S2[1:]:
        PV.append(PV[-1] + val)
    PV = np.asarray(PV)
    PV = PV/sumS
    return PV

# get k that satisfies proportion of variance
def get_k(S, pvar):
    PV = percent_var(S)
    for k,var in enumerate(PV):
        if var >= pvar:
            break
    return k+1

# creates diagonal matrix from array
def diag(S):
    import numpy as np
    rank = len(S)
    Sig = [[0 for x in range(rank)] for y in range(rank)]
    for i in range(rank):
        Sig[i][i] = S[i]
    return np.asmatrix(Sig)
