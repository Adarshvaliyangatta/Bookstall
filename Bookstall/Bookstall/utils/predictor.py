from sklearn.linear_model import LinearRegression
import numpy as np

hours=np.array([[1],[2],[3],[4],[5]])

bill=np.array([180,360,540,720,900])

model=LinearRegression()

model.fit(hours,bill)

def predict_bill(items):

    return round(model.predict([[items]])[0],2)