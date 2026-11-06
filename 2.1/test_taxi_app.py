import unittest
import taxi_app

class TestTaxiApp(unittest.TestCase):
    
    def setUp(self):
        """Ініціалізація тестових даних перед кожним тестом"""
        self.drivers = [
            {"name": "Олександр", "rating": 4.8, "available": True},
            {"name": "Андрій", "rating": 4.2, "available": True}
        ]

    def test_calculate_fare_positive(self):
        """Позитивний тест: коректний розрахунок вартості поїздки"""
        fare = taxi_app.calculate_fare(10, base_fare=50, rate_per_km=10)
        self.assertEqual(fare, 150)

    def test_calculate_fare_negative(self):
        """Негативний тест: перевірка викиду ValueError при від'ємній відстані"""
        with self.assertRaises(ValueError):
            taxi_app.calculate_fare(-5)

    def test_add_driver_exception(self):
        """Негативний тест: перевірка рейтингу, що виходить за межі 5.0"""
        with self.assertRaises(ValueError):
            taxi_app.add_driver(self.drivers, "Максим", 6.2)

    def test_assign_driver(self):
        """Позитивний тест: успішне призначення водія"""
        result = taxi_app.assign_driver(self.drivers, "Данило")
        self.assertIn("Олександр", result)

    def test_assign_driver_no_available(self):
        """Негативний тест: виключення, якщо немає вільних водіїв"""
        busy_drivers = [{"name": "Олександр", "rating": 4.8, "available": False}]
        with self.assertRaises(Exception):
            taxi_app.assign_driver(busy_drivers, "Данило")
    
    @unittest.expectedFailure
    def test_calculate_fare_expected_failure(self):
        fare = taxi_app.calculate_fare(10, base_fare=50, rate_per_km=10)
        self.assertEqual(fare, 151)
    
    @unittest.expectedFailure
    def test_assign_driver(self):
        result = taxi_app.assign_driver(self.drivers, "Данило")
        self.assertIn("Олександрп", result)

if __name__ == '__main__':
    unittest.main()