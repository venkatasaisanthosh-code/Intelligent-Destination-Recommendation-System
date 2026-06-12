import pandas as pd

df = pd.read_csv("datasets/destinations.csv")

def recommend(category,max_budget):

    results = df[
        (df["Category"] == category)
        &
        (df["Budget"] <= max_budget)
    ]

    return results.sort_values(
        by="Rating",
        ascending=False
    )