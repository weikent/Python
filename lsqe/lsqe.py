#!/usr/bin/env python

import sys

def lsqe(X_name, Y_name):
    """
    
    Arguments:
    - `self`:
    """
    

    

    X = open(X_name).readline()
    x_arr = X.strip().split(' ')
    n = len(x_arr)

    Y = open(Y_name).readline()
    y_arr = Y.strip().split(' ')




    sumx = 0.0
    sumy = 0.0
    sumx2 = 0.0
    sumxy = 0.0

    for i in range(n):
        sumx = sumx + float(x_arr[i])
        sumy = sumy + float(y_arr[i])
        sumx2 = sumx2 + (float(x_arr[i]) ** 2)
        sumxy = sumxy + (float(x_arr[i]) * float(y_arr[i]))



    k = (sumxy - ((sumx * sumy)/n)) / (sumx2-((sumx ** 2)/n));
    b = (sumy - ((k) * sumx)) / n;


    print "k = %.15f , b = %.15f" % (k, b)
    return "k = %.15f , b = %.15f" % (k, b)


if __name__ == '__main__':
    X_name = sys.argv[1]
    Y_name = sys.argv[2]
    lsqe(X_name, Y_name)
    
