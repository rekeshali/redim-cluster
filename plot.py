import os
import numpy as np
import matplotlib.pyplot as mp

def var_plot(S,k,see):
    from tools import percent_var
    PV = percent_var(S)
    d = range(len(S)+1)[1:] 
    fig = mp.figure()

    ax = fig.add_subplot(211)
    ax.axvline(x=k)
    ax.plot(d,S/max(S))
    ax.scatter(d,S/max(S))

    ax = fig.add_subplot(212)
    ax.axvline(x=k)
    ax.plot(d,PV)
    ax.scatter(d,PV)

    figname = 'varplot.png'
    mp.savefig(figname)
    if see:
        os.system('see ' + figname)
#     mp.show()

def pc_plot(S,U,see):
    W1 = S[0]*U[:,0]
    W2 = S[1]*U[:,1]
#     W1 = U[:,0]
#     W2 = U[:,1]
    fig = mp.figure()
    size = U.shape

    ax = fig.add_subplot(111)
    ax.scatter(W1,W2, color='r')
    for N in range(size[1]):
        mp.text(W1[N], W2[N], str(N), fontsize=12)
    ax.axis('equal')

    figname = 'pcplot.png'
    mp.savefig(figname)
    if see:
        os.system('see ' + figname)
#     mp.show()
