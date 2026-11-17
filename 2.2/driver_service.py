from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Driver Service")

# Звичайна база даних у пам'яті
drivers_list = [
    {"id": 1, "name": "Олександр", "rating": 4.8, "available": True},
    {"id": 2, "name": "Андрій", "rating": 4.2, "available": True},
    {"id": 3, "name": "Максим", "rating": 4.9, "available": False}
]

# Спеціальна модель для створення нового водія через запит
class DriverCreate(BaseModel):
    name: str
    rating: float

@app.get("/drivers")
def get_drivers():
    return {"drivers": drivers_list}

@app.get("/drivers/available")
def get_available_drivers():
    available = [d for d in drivers_list if d["available"]]
    return {"available_drivers": available}

# --- НОВІ ЕНДПОІНТИ ДЛЯ КЕРУВАННЯ ---

@app.post("/drivers")
def add_driver(driver: DriverCreate):
    """Додає нового водія до системи"""
    new_id = len(drivers_list) + 1
    new_driver = {
        "id": new_id,
        "name": driver.name,
        "rating": driver.rating,
        "available": True # Новий водій за замовчуванням вільний
    }
    drivers_list.append(new_driver)
    return {"message": "Водія успішно додано", "driver": new_driver}

@app.patch("/drivers/{driver_id}/status")
def update_driver_status(driver_id: int, available: bool):
    """Змінює статус водія (вільний/зайнятий) за його ID"""
    for driver in drivers_list:
        if driver["id"] == driver_id:
            driver["available"] = available
            return {"message": f"Статус водія {driver['name']} оновлено", "available": driver["available"]}
    
    raise HTTPException(status_code=404, detail="Водія з таким ID не знайдено")