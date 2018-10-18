import os
import numpy as np
import matplotlib.pyplot as mp

def var_plot(S,k,see):
    from tools import percent_var
    # get percent of variance for k singular values
    PV = percent_var(S)
    d = range(len(S)+1)[1:] 

    # prepare to plot
    fig = mp.figure()

    # scree graph
    ax = fig.add_subplot(211)
    ax.set(title='Scree Graph',xlabel='Singular Vector',ylabel='Singular Value')
    ax.axvline(x=k) # vertical line at choice of k
    ax.plot(d,S)
    ax.scatter(d,S,marker='+')
    mp.text(k+0.5, (max(S)+min(S))/2, 'k = ' + str(k))

    # proportion of variance vs k 
    ax = fig.add_subplot(212)
    ax.set(title='Proportion of Variance',xlabel='First Singular Vectors',ylabel='Prop. of Var.')
    ax.axvline(x=k)
    ax.plot(d,PV)
    ax.scatter(d,PV,marker='+')
    mp.text(k+0.5, (max(PV)+min(PV))/2, 'k = ' + str(k))

    # post plot
    fig.subplots_adjust(hspace=0.5)
    fig.tight_layout()

    # save fig and view
    figname = 'varplot.png'
    mp.savefig(figname)
    if see:
        os.system('see ' + figname)
#     mp.show()

def pc_plot(S,U,see):
    # get 1st and 2nd principal components
    W1 = S[0]*U[:,0]
    W2 = S[1]*U[:,1]
    ninst = len(W1)
#     W1 = U[:,0]
#     W2 = U[:,1]

    # prepare to plot
    fig = mp.figure() # make fig
    ax = fig.add_subplot(111) # make axes
    mp.grid(True)
    ax.axis('equal') # equally proportioned axes
    ax.set(xlabel='First Principal Component',ylabel='Second Principal Component')

    # plotting
    ax.scatter(W1,W2, color='r') # plot points in red
    for n in range(ninst): # label points by school's number in list
        mp.text(W1[n], W2[n], str(n), fontsize=12)

    # post plot
    fig.tight_layout()

    # save fig and view 
    figname = 'pcplot.png' 
    mp.savefig(figname)
    if see: # open png in preview
        os.system('see ' + figname) # see not included
#     mp.show()

def pcc_plot(S,U,C,see):
    # get 1st and 2nd principal components

    # prepare to plot
    fig = mp.figure() # make fig
    ax = fig.add_subplot(111) # make axes
    mp.grid(True)
    ax.axis('equal') # equally proportioned axes
    ax.set(xlabel='First Principal Component',ylabel='Second Principal Component')

    key = C.keys()
    for tooth in key:
        W1 = S[0]*U[C[tooth],0]
        W2 = S[1]*U[C[tooth],1]
        col = 'C' + tooth
        ax.scatter(W1,W2,color=col)
        for idx,n in enumerate(C[tooth]):
            mp.text(W1[idx], W2[idx], str(n), fontsize=12)

    # post plot
    fig.tight_layout()

    # save fig and view 
    figname = 'pcplot.png' 
    mp.savefig(figname)
    if see: # open png in preview
        os.system('see ' + figname) # see not included
#     mp.show()
