#!/usr/bin/python
from explore import key, db
from prepare import znorm
from implement import svd, reduct, kmeans
from tools import buildX, get_k
from plot import var_plot, pc_plot, pcc_plot

####### PART 1: Principal Component Analysis ####################
# preparation
bools = [True, False]
norm = bools[0] # normalize bool
see  = bools[1] # show figures bool
pvar = 0.9 # percent of variance captured by k singular values
if norm:
    db = znorm() # z-normalize

# finding reduced dimensions
[U, S, Vh] = svd(db) # perform SVD
k = get_k(S, pvar) # find k singular values that satisfies pvar

# plotting
var_plot(S,k,see) # scree, var vs eigens
pc_plot(S,U,see) # first and second pc's scaled by sigma

####### PART 2: k-Means Clustering ##############################
kc = 7 # number of clusters
see = bools[0]

## Full dataset
X = buildX(db)
[CF,iF] = kmeans(kc,X)
pcc_plot(S,U,CF,see)

## First k singular vectors
Xk = reduct(U, S, Vh, k) # reduced order matrix
[Ck,ik] = kmeans(kc,Xk)
pcc_plot(S,U,Ck,see)

## First 2 singular vectors
X2 = reduct(U, S, Vh, 2) # reduced order matrix
[C2,i2] = kmeans(kc,X2)
pcc_plot(S,U,C2,see)
