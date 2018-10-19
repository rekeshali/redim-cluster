#!/usr/bin/python

# get mean and standard deviation of attribute
def stats():
    import numpy as np
    from explore import db, key
    dbst = {}
    for tooth in key:
        dbst[tooth] = []
        dbst[tooth].append(np.mean(db[tooth]))
        dbst[tooth].append(np.std( db[tooth]))
    return dbst

# standardize data using z-norm
def znorm():
    from explore import db, key
    dbst = stats()
    dbz = {}
    for tooth in key:
        dbz[tooth] = []
        for val in db[tooth]:
            dbz[tooth].append( (val - dbst[tooth][0])/dbst[tooth][1] )
    return dbz
