import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
def resistant_line (X,Y):
    first_third_X = X [:int(len(X)/3)]
    last_third_X = X [int(2*len(X)/3):]
    first_third_Y = Y [:int(len(X)/3)]
    last_third_Y = Y [int(2*len(X)/3):]

    first_anchor_X = np.median(first_third_X)
    first_anchor_Y = np.median(first_third_Y)
    second_anchor_X = np.median(last_third_X)
    second_anchor_Y = np.median(last_third_Y)

    b= (second_anchor_Y-first_anchor_Y)/(second_anchor_X-first_anchor_X)
    r = Y-b*X
    a=np.median(r)
    return a,b

if __name__ == "__main__":
    df = pd.read_csv("heights.csv")
    df = df.sort_values(by=['HEIGHT'])
    X = df['HEIGHT'].to_numpy()[:-1]
    Y = df['WEIGHT'].to_numpy()[:-1]
    plt.scatter(X,Y,color="green")
    plt.show()

    plt.scatter(X,Y,color="green")
    aRL,bRL = resistant_line (X,Y)
    X_RL= np.append(X,0)
    plt.plot(X_RL,aRL+bRL*X_RL,color="red")

    bLS= np.sum((Y-Y.mean())*(X-X.mean()))/np.sum((X-X.mean())**2)
    aLS = Y.mean() - X.mean() * bLS
    plt.plot(np.append(X,0),aLS+bLS*np.append(X,0),color="blue")
    plt.show()

    print("bLS=",bLS)
    r=np.sum((Y-Y.mean())*(X-X.mean()))/math.sqrt(np.sum((X-X.mean())**2)*np.sum((Y-Y.mean())**2))
    print("r=",r)
    print("r_square=",(r**2)*100)

