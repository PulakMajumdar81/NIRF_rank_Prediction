import numpy as np
import pandas as pd 
import math 

def rank_prediction(score):
    dataset=pd.read_csv("C:\\Users\\USER\\Desktop\\NIRF2021.csv")
    X=dataset.iloc[:,:-1].values
    y=dataset.iloc[:,1].values
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.1,random_state=0)
    from sklearn.linear_model import LinearRegression
    from sklearn.preprocessing import PolynomialFeatures
    poly=PolynomialFeatures(degree =4)
    X_poly=poly.fit_transform(X_train)
    poly.fit(X_poly,y_train)
    lin2=LinearRegression()
    lin2.fit(X_poly,y_train)
    y_train_predicted=lin2.predict(X_poly)

    y_pred=(lin2.predict(poly.fit_transform([[score]])))
    predicted=math.floor(y_pred)
    return predicted
    


