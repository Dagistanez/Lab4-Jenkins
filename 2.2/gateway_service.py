from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI(title="Order Gateway Service")

# Правильні адреси мікросервісів усередині Docker мережі
DRIVER_SERVICE_URL = "http://driver-service:8000"
FARE_SERVICE_URL = "http://fare-service:8001"

@app.post("/order")
def create_taxi_order(distance_km: float):
    """
    Створює замовлення таксі: зв'язується з сервісом тарифів і сервісом водіїв.
    """
    try:
        # 1. Запитуємо розрахунок ціни у Fare Service
        with httpx.Client() as client:
            fare_response = client.get(
                f"{FARE_SERVICE_URL}/calculate",
                params={"distance_km": distance_km}
            )
        
        if fare_response.status_code != 200:
            raise HTTPException(status_code=400, detail="Помилка при розрахунку тарифу")
        
        fare_data = fare_response.json()

        # 2. Отримуємо список вільних водіїв з Driver Service
        with httpx.Client() as client:
            drivers_response = client.get(f"{DRIVER_SERVICE_URL}/drivers/available")
            
        if drivers_response.status_code != 200:
            raise HTTPException(status_code=400, detail="Не вдалося отримати список водіїв")
            
        available_drivers = drivers_response.json().get("available_drivers", [])

        if not available_drivers:
            raise HTTPException(status_code=404, detail="На жаль, зараз немає вільних водіїв")

        # Призначаємо першого вільного водія з отриманого списку
        assigned_driver = available_drivers[0]

        # 3. Формуємо фінальну відповідь замовлення
        return {
            "status": "Success",
            "order_details": {
                "distance_km": distance_km,
                "total_fare": fare_data["total_fare"],
                "assigned_driver": assigned_driver["name"],
                "driver_rating": assigned_driver["rating"]
            }
        }

    except httpx.RequestError:
        raise HTTPException(status_code=503, detail="Один із мікросервісів недоступний")
    