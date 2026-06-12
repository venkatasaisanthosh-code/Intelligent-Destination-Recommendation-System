import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

df = pd.read_csv("../datasets/destinations.csv")

X = df[["Days","Rating"]]
y = df["Budget"]

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X,y)

joblib.dump(model,"budget_model.pkl")

print("Model Saved")