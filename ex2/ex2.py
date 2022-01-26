import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math


def  kernel_density(x,h,color):
    t = np.linspace(start=np.min(x)-h,stop=np.max(x)+h,num=len(x))
    w_norm_vec = np.vectorize(w_norm,excluded=[1])
    j = w_norm_vec(t, x, h)
    plt.plot(t,j,color=color)

def w_norm (a,x,h):
    vector=(x-a)/h
    w_vectorized = np.vectorize(w)
    return np.average(w_vectorized(vector))/h


def w(u):
    return (1+math.cos(2*math.pi*u)) if abs(u)<=0.5 else 0.0

if __name__ == "__main__":
    df = pd.read_csv("grades.csv")

    h=12


    #Q1e
    kernel_density(df['gym'],h,'red')
    plt.xlim(0,100)
    plt.show()

    for school,color in zip(['A','B','C'],['red','blue','green']):
        kernel_density(df[df['school'] == school]['gym'], h,color)
        plt.xlim(0,100)
    plt.show()

    df = pd.read_csv("grades.csv")
    # Q1b
    kernel_density(df['math'],12,'red')
    plt.show()

    h=12

    # Q1d
    for school,color in zip(['A','B','C'],['red','blue','green']):
        kernel_density(df[df['school'] == school]['math'], h,color)
    plt.show()




