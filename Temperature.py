import pandas as pd 
data = pd.read_csv("aqms.csv").fillna(data[['Temperature']].median()).fillna(data[['CO_AQI']].median()).fillna(data[['NO2_AQI']].median()).fillna(data[['SO2_AQI']].median())
x = data[['CO_AQI','NO2_AQI','SO2_AQI']]
y = data[['Temperature']]
model = linear_model.LinearRegression()
model.fit(x,y)

print("Temperature : ",model.predict([[158,0.13,270]]))
