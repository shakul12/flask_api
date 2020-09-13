import pandas as pd 
from sklearn.linear_model import LinearRegression
import pickle

df= pd.read_csv("data.csv")


predict= df.iloc[:,:1].values
x= df.iloc[:,1:].values

lin=LinearRegression()
lin.fit(x,predict)


pickle.dump(lin,open("model.sav","wb"))
