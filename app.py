import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import
mean_absolute_error,mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
data=pd.DataFrame({'WindSpeed':[5,7,10,12,6,8,15,9,11,14],'Temper
ature':[30,32,35,28,31,29,27,33,34,26],'PowerOutput':[100,150,300,3
50,120,200,400,220,310,380]})
X=data[['WindSpeed','Temperature']]
y=data['PowerOutput']
reg_model=LinearRegression()
reg_model.fit(X,y)
predictions=reg_model.predict(X)
print("MAE:",mean_absolute_error(y,predictions))
print("RMSE:",np.sqrt(mean_squared_error(y,predictions)))
theft_data=pd.DataFrame({'Consumption':[100,120,500,130,600,110
,105,700,115,125],'Theft':[0,0,1,0,1,0,0,1,0,0]})

AI-Based Smart Grid Optimization Using Machine Learning:

X=theft_data[['Consumption']]
y=theft_data['Theft']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random
_state=42)
clf_model=RandomForestClassifier(n_estimators=100,random_state=
42)
clf_model.fit(X_train,y_train)
print("Accuracy:",clf_model.score(X_test,y_test))
voltage_data=np.array([[220],[222],[219],[400],[221],[405],[218],[4
10]])
kmeans=KMeans(n_clusters=2,random_state=42,n_init=10)
kmeans.fit(voltage_data)
print("Cluster Labels:",kmeans.labels_)
plt.scatter(range(len(voltage_data)),voltage_data,c=kmeans.labels_)
plt.xlabel("Sample Index")
plt.ylabel("Voltage")
plt.title("Fault Detection")
plt.show()
