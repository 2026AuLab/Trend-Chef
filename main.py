from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="TrendChef — Live")

class Recipe(BaseModel):
    dish_name: str
    ingredients: str
    method: str
    trend_score: int

@app.get("/recipe")
def full_recipe():
    return {
        "dish_name": "Yuzu Miso Glazed Salmon",
        "ingredients": "180g salmon, 45ml yuzu, 30g miso, 15g ginger",
        "method": "1. Mix marinade. 2. Marinate 20 min. 3. Grill 4 min per side.",
        "trend_score": 97,
        "growth": "+412%"
    }

@app.get("/generate")
def generator(style: str = "Fine Dining"):
    return {
        "variations": [
            "Yuzu Miso Duck Breast (Mishlen)",
            "Vegan Yuzu Tofu Bowl",
            "Budget Yuzu Chicken for Bar"
        ]
    }

@app.get("/vision")
def vision():
    return {"dish_name": "Yuzu Miso Salmon", "cuisine": "Modern Australian-Japanese", "confidence": 94}

@app.get("/trend")
def trend():
    return {"score": 97, "growth": "+412%", "sentiment": "very positive"}
