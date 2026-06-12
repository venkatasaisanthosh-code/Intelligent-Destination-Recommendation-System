import streamlit as st
import joblib

from utils.recommender import recommend
from utils.itinerary_generator import generate_itinerary

model = joblib.load(
    "models/budget_model.pkl"
)

st.title("AI Travel Planner For Students")

category = st.selectbox(
    "Travel Type",
    [
        "Beach",
        "Hill Station",
        "Historical",
        "City",
        "Mountain"
    ]
)

days = st.slider(
    "Trip Duration",
    1,
    7,
    3
)

rating = st.slider(
    "Preferred Rating",
    3.0,
    5.0,
    4.5
)

budget_prediction = model.predict(
    [[days,rating]]
)[0]

st.write(
    f"Estimated Budget: ₹{int(budget_prediction)}"
)

if st.button("Find Destinations"):

    places = recommend(
        category,
        budget_prediction
    )

    st.dataframe(places)

    if len(places) > 0:

        destination = places.iloc[0]["Destination"]

        itinerary = generate_itinerary(
            destination,
            int(budget_prediction),
            days
        )

        st.subheader(
            "Generated Itinerary"
        )

        st.write(itinerary)