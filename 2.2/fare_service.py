from fastapi import FastAPI, HTTPException

app = FastAPI(title="Fare Service")

@app.get("/calculate")
def calculate_fare(distance_km: float, base_fare: float = 50.0, rate_per_km: float = 15.0):
    """
    Раховує вартість поїздки на основі дистанції, подачі та тарифу за кілометр.
    """
    if distance_km < 0:
        raise HTTPException(status_code=400, detail="Відстань не може бути від'ємною")
    
    total_fare = base_fare + (distance_km * rate_per_km)
    return {
        "distance_km": distance_km,
        "base_fare": base_fare,
        "rate_per_km": rate_per_km,
        "total_fare": total_fare
    }