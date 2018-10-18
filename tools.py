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

def get_k(S, pvar):
    PV = percent_var(S)
    for k,var in enumerate(PV):
        if var >= pvar:
            break
    return k+1
