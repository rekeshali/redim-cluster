#!/usr/bin/python
from explore import key, db
from prepare import znorm
from implement import buildX, svd, reduct
from tools import get_k
from plot import var_plot, pc_plot

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

# reducing dimensions
X  = buildX(db) # create data matrix
Xk = reduct(U, S, Vh, k) # reduced order matrix

# plotting
var_plot(S,k,see) # scree, var vs eigens
pc_plot(S,U,see) # first and second pc's scaled by sigma

####### PART 2: k-Means Clustering ##############################

