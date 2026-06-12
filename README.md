# AI Travel Planner

An intelligent travel planning application that uses machine learning to recommend destinations, generate itineraries, and predict travel budgets.

## Features

- **Destination Recommendations**: Get personalized travel destination recommendations based on budget, climate preferences, and activities
- **Itinerary Generation**: Automatically generate day-by-day travel itineraries
- **Budget Prediction**: ML-based budget forecasting for trips
- **Destination Information**: Detailed information about various travel destinations

## Project Structure

```
AI_Travel_Planner/
├── app.py                    # Main Flask application
├── models/
│   ├── train_model.py       # Model training script
│   └── budget_model.pkl     # Pre-trained budget prediction model
├── datasets/
│   └── destinations.csv     # Destination dataset
├── utils/
│   ├── recommender.py       # Travel recommendation engine
│   └── itinerary_generator.py # Itinerary generation module
├── requirements.txt          # Project dependencies
└── README.md                 # This file
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd AI_Travel_Planner
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

### Training the Model

To train the budget prediction model:

```bash
cd models
python train_model.py
```

## API Endpoints

- `GET /` - Home page
- `POST /api/recommend` - Get travel recommendations
- `POST /api/generate-itinerary` - Generate a travel itinerary
- `POST /api/predict-budget` - Predict travel budget

## Example Usage

### Get Recommendations
```bash
curl -X POST http://localhost:5000/api/recommend \
  -H "Content-Type: application/json" \
  -d '{"budget": 1500, "climate": "Tropical"}'
```

### Generate Itinerary
```bash
curl -X POST http://localhost:5000/api/generate-itinerary \
  -H "Content-Type: application/json" \
  -d '{"destination": "Bali", "duration": 5, "type": "beach"}'
```

### Predict Budget
```bash
curl -X POST http://localhost:5000/api/predict-budget \
  -H "Content-Type: application/json" \
  -d '{"duration": 7, "destination": "Paris"}'
```

## Technologies Used

- **Python** - Core programming language
- **Flask** - Web framework
- **Pandas** - Data manipulation
- **Scikit-learn** - Machine learning
- **NumPy** - Numerical computing

## Contributing

Feel free to fork this project and submit pull requests for any improvements.

## License

This project is licensed under the MIT License.
