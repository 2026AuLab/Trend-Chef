from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="TrendChef — Live Version")

@app.get("/")
def home():
    return {"status": "✅ TrendChef работает!", "message": "Привет, шеф! Это твой первый живой endpoint."}

@app.get("/recipe")
def full_recipe():
    return {
        "dish_name": "Yuzu Miso Glazed Salmon",
        "ingredients": "180g salmon fillet, 45ml yuzu juice, 30g white miso, 15g grated ginger, 10ml sesame oil",
        "method": "1. Mix yuzu, miso, ginger and sesame oil. 2. Marinate salmon 20 min. 3. Grill 4 min each side at 180°C. 4. Rest 2 min. Serve with pickled cucumber.",
        "prep_time": 15,
        "cook_time": 8,
        "trend_score": 97,
        "growth": "+412% in Brisbane"
    }

@app.get("/generate")
def generate_variation(style: str = "Fine Dining"):
    return {
        "variations": [
            f"1. Yuzu Miso Duck Breast (for {style})",
            f"2. Vegan Yuzu Tofu with Macadamia (for {style})",
            f"3. Budget Yuzu Chicken Skewers (for {style})"
        ]
    }

@app.get("/trends")
def trends():
    return {
        "trend_of_day": "Yuzu Miso Salmon from The Fifty Six",
        "growth": "+412%",
        "restaurant": "The Fifty Six",
        "score": 97
    }
