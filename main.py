from fastapi import FastAPI

app = FastAPI(title="TrendChef")

@app.get("/")
def home():
    return {"status": "✅ Работает!", "message": "TrendChef запущен в Брисбене! Тренд дня: Yuzu Miso Salmon +412%"}

@app.get("/trends")
def trends():
    return {"trend": "Yuzu Miso Salmon", "restaurant": "The Fifty Six", "growth": "+412%"}
