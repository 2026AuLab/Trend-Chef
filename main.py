from fastapi import FastAPI

app = FastAPI(title="TrendChef — Live")

@app.get("/")
def home():
    return {"status": "✅ Работает!", "message": "TrendChef в Брисбене запущен"}

@app.get("/recipe")
def full_recipe():
    return {
        "dish_name": "Yuzu Miso Glazed Salmon",
        "ingredients": "180g salmon, 45ml yuzu juice, 30g white miso, 15g ginger",
        "method": "1. Mix marinade. 2. Marinate 20 min. 3. Grill 4 min each side.",
        "prep_time": 15,
        "cook_time": 8,
        "trend_score": 97
    }

@app.get("/generate")
def generate():
    return {"variations": ["Yuzu Duck", "Vegan Tofu", "Budget Chicken"]}

@app.get("/trends")
def trends():
    return {"trend": "Yuzu Miso Salmon", "growth": "+412%", "score": 97}
