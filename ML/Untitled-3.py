#%%
from numpy.lib.index_tricks import fill_diagonal
import pandas as pd
import numpy as np
from sklearn import tree 

print("Hello, lets change the world!")
df = pd.read_csv("MLDataTest.csv")
print(df)
## First I need to add the median value for ever 'NaN' Value 
        # Replaceing The 'NaN' values for Civil Liberties.
mean1 = df['Country A Civil Liberties'].mean(); df['Country A Civil Liberties'] = df['Country A Civil Liberties'].fillna(mean1)
mean2 = df['Country B Civil Liberties'].mean(); df['Country B Civil Liberties'] = df['Country B Civil Liberties'].fillna(mean2)
mean3 = df['Country C Civil Liberties'].mean(); df['Country C Civil Liberties'] = df['Country C Civil Liberties'].fillna(mean3)
mean4 = df['Country D Civil Liberties'].mean(); df['Country D Civil Liberties'] = df['Country D Civil Liberties'].fillna(mean4)
mean5 = df['Country E Civil Liberties'].mean(); df['Country E Civil Liberties'] = df['Country E Civil Liberties'].fillna(mean5)
mean6 = df['Country F Civil Liberties'].mean(); df['Country F Civil Liberties'] = df['Country F Civil Liberties'].fillna(mean6)
        # Replacing the 'NaN' values for % Military Spending.
mean7 = df['Country A Military Spending'].mean(); df['Country A Military Spending'] = df['Country A Military Spending'].fillna(mean7)
mean8 = df['Country B Military Spending'].mean(); df['Country B Military Spending'] = df['Country B Military Spending'].fillna(mean8)
mean9 = df['Country C Military Spending'].mean(); df['Country C Military Spending'] = df['Country C Military Spending'].fillna(mean9)
mean10 = df['Country D Military Spending'].mean(); df['Country D Military Spending'] = df['Country D Military Spending'].fillna(mean10)
mean11 = df['Country E Military Spending'].mean(); df['Country E Military Spending'] = df['Country E Military Spending'].fillna(mean11)
mean12 = df['Country F Military Spending '].mean(); df['Country F Military Spending'] = df['Country F Military Spending '].fillna(mean12)
        #Replacing the 'Nan' values for GDP 2010 constant dollars.
mean13 = df['Country A GDP '].mean(); df['Country A GDP '] = df['Country A GDP '].fillna(mean13) 
mean15 = df['Country B GDP'].mean(); df['Country B GDP'] = df['Country B GDP'].fillna(mean15) # yes I notitced I skiped a number opps... :p
mean16 = df['Country C GDP'].mean(); df['Country C GDP'] = df['Country C GDP'].fillna(mean16)
mean17 = df['Country D GDP'].mean(); df['Country D GDP'] = df['Country D GDP'].fillna(mean17)
mean18 = df['Country E GDP'].mean(); df['Country E GDP'] = df['Country E GDP'].fillna(mean18)
mean19 = df['Country F GDP'].mean(); df['Country F GDP'] = df['Country F GDP'].fillna(mean19)
print(df)