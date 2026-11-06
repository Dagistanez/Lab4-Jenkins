import sys
drivers = []

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

def main():
    """Інтерактивне меню для запуску в Docker"""
    # Додамо парочку водіїв для старту
    add_driver(drivers, "Олександр", 4.9)
    add_driver(drivers, "Михайло", 4.7)

    while True:
        print("\n=== КОНСОЛЬНИЙ СЕРВІС ТАКСІ (Варіант 7) ===")
        print("1. Показати всіх водіїв")
        print("2. Додати нового водія")
        print("3. Розрахувати вартість поїздки")
        print("4. Призначити водія клієнту")
        print("5. Фільтрувати водіїв за рейтингом")
        print("6. Вихід")
        
        choice = input("Оберіть пункт меню (1-6): ")
        
        try:
            if choice == "1":
                print("\nСписок водіїв:")
                for i, d in enumerate(drivers, 1):
                    status = "Вільний" if d["available"] else "На замовленні"
                    print(f"{i}. Ім'я: {d['name']} | Рейтинг: {d['rating']} | Статус: {status}")
            
            elif choice == "2":
                name = input("Введіть ім'я водія: ")
                rating = float(input("Введіть рейтинг (1.0 - 5.0): "))
                add_driver(drivers, name, rating)
                print(f"Водія {name} успішно додано!")
            
            elif choice == "3":
                dist = float(input("Введіть відстань у км: "))
                fare = calculate_fare(dist)
                print(f"Вартість поїздки: {fare} грн")
            
            elif choice == "4":
                client = input("Введіть ім'я клієнта: ")
                result = assign_driver(drivers, client)
                print(result)
            
            elif choice == "5":
                min_r = float(input("Введіть мінімальний рейтинг для фільтру: "))
                top_d = filter_top_drivers(drivers, min_r)
                print("\nЗнайдені водії:")
                for d in top_d:
                    print(f"- {d['name']} (Рейтинг: {d['rating']})")
            
            elif choice == "6":
                print("Вихід з програми...")
                sys.exit(0)
            else:
                print("Невірний вибір. Спробуйте від 1 до 6.")
        except Exception as e:
            print(f"[Помилка]: {e}")

if __name__ == "__main__":
    main()