import pandas as pd
import numpy as np
from sklearn import datasets

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,LogisticRegression
import pickle

df = pd.read_csv('DataSet/datasetUdara_clean.csv')
f = ["pm10", "so2", "co", "o3", "no2"]
g = {"categori": {"BAIK": 2, "SEDANG": 1, "TIDAK SEHAT": 0}}
df.replace(g, inplace= True)

dataa = df[f]; X = dataa.to_numpy()
target = df[g]; y = target.to_numpy();y = y.ravel()

x_train,x_test,y_train,y_test=train_test_split(X,y)
lin_reg=LinearRegression()
log_reg=LogisticRegression(solver='lbfgs', max_iter=1000)

lin_reg=lin_reg.fit(x_train,y_train)
log_reg=log_reg.fit(x_train,y_train)

pickle.dump(lin_reg,open('lin_model.pkl','wb'))
pickle.dump(log_reg,open('log_model.pkl','wb'))


