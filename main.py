from supabase import create_client, Client
supabase: Client = create_client(
    "https://gyvcqkoufedoiwftteubv.supabase.co",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imd5dmNxa291ZmVkb2l3ZnRldWJ2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODE3ODMwNjksImV4cCI6MjA5NzM1OTA2OX0.ep8Lvesr0LtoG0QCI0oyk9tPus8dd56Vm8SeAYAkORo"
)

@app.get("/save_recipe")
def save():
    data = {"dish": "Yuzu Salmon", "chef": "Alex"}
    result = supabase.table("dishes").insert(data).execute()
    return {"saved": result.data}
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
# Добавь к существующему коду
@app.get("/vision")
def vision_analysis():
    return {"dish_name": "Yuzu Miso Salmon", "cuisine_style": "Modern Australian-Japanese", "category": "Main", "main_ingredients": "salmon, yuzu, miso", "cooking_techniques": "grill, marinade", "confidence": 96}

@app.get("/analysis")
def trend_analysis():
    return {"trend_score": 97, "growth_rate": 412, "sentiment": "very positive", "key_reasons": "Instagram viral, Queensland seafood", "recommendation": "Add to menu today"}

@app.get("/pairing")
def pairing():
    return {"garnish": "pickled cucumber + edible flowers", "pairing_suggestion": "Chardonnay or sake"}
