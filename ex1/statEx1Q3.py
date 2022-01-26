from scipy.stats import binom
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



if __name__ == '__main__':
    df = pd.read_csv("appendicitis.csv")
    total =df['Pathology'].count()#counting total number of patients
    wrong = df[df['Pathology']==2].count()[0] #counting total number of "Pathology =2"
    print (wrong/total) #
    print(df.groupby(['Sex','Pathology']).count()) #table



