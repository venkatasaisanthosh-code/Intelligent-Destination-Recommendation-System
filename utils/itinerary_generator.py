import google.generativeai as genai

genai.configure(api_key="")

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_itinerary(destination,budget,days):

    prompt = f"""
    Create a student-friendly itinerary.

    Destination: {destination}
    Budget: {budget}
    Days: {days}

    Include:
    - Day wise plan
    - Budget breakdown
    - Food suggestions
    - Transportation
    """

    response = model.generate_content(prompt)

    return response.text