def add_driver(drivers_list, name, rating):
    """Додає нового водія до списку з перевіркою валідності рейтингу."""
    if rating < 1.0 or rating > 5.0:
        raise ValueError("Рейтинг повинен бути в межах від 1.0 до 5.0")
    drivers_list.append({"name": name, "rating": rating, "available": True})
    return drivers_list

def calculate_fare(distance_km, base_fare=50, rate_per_km=15):
    """Обчислює вартість поїздки на таксі."""
    if distance_km < 0:
        raise ValueError("Відстань не може бути від'ємною")
    return base_fare + (distance_km * rate_per_km)

def assign_driver(drivers_list, client_name):
    """Призначає першого доступного водія клієнту."""
    available_drivers = [d for d in drivers_list if d["available"]]
    if not available_drivers:
        raise Exception("Немає доступних водіїв на лінії")
    
    driver = available_drivers[0]
    driver["available"] = False
    return f"Водій {driver['name']} призначений для клієнта {client_name}"

def filter_top_drivers(drivers_list, min_rating):
    """Фільтрує водіїв із високим рейтингом."""
    if min_rating < 0 or min_rating > 5.0:
        raise ValueError("Некоректне значення мінімального рейтингу")
    return [d for d in drivers_list if d["rating"] >= min_rating]

def cancel_trip(driver):
    """Скасовує поїздку та робить водія знову доступним."""
    driver["available"] = True
    return "Поїздку скасовано, водій вільний"