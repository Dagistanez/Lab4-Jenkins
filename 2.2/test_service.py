import unittest
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from gateway_service import app
import xmlrunner

client = TestClient(app)

class TestGatewayService(unittest.TestCase):


    @patch("gateway_service.httpx.Client")
    def test_create_taxi_order_success(self, mock_httpx_client):
        """Тест успішного створення замовлення через шлюз"""
        mock_instance = mock_httpx_client.return_value.__enter__.return_value
        
        def mock_get_side_effect(url, params=None):
            response_mock = MagicMock()
            if "/calculate" in url:
                response_mock.status_code = 200
                response_mock.json.return_value = {"total_fare": 150}
            elif "/drivers/available" in url:
                response_mock.status_code = 200
                response_mock.json.return_value = {
                    "available_drivers": [{"name": "Олександр", "rating": 4.9}]
                }
            return response_mock

        mock_instance.get.side_effect = mock_get_side_effect

        response = client.post("/order", params={"distance_km": 10})

        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "Success"
        assert data["order_details"]["total_fare"] == 150
        assert data["order_details"]["assigned_driver"] == "Олександр"

    @patch("gateway_service.httpx.Client")
    def test_create_taxi_order_no_drivers(self, mock_httpx_client):
        """Тест ситуації, коли немає вільних водіїв (очікуємо 404)"""
        mock_instance = mock_httpx_client.return_value.__enter__.return_value
        
        def mock_get_side_effect(url, params=None):
            response_mock = MagicMock()
            if "/calculate" in url:
                response_mock.status_code = 200
                response_mock.json.return_value = {"total_fare": 150}
            elif "/drivers/available" in url:
                response_mock.status_code = 200
                response_mock.json.return_value = {"available_drivers": []}
            return response_mock

        mock_instance.get.side_effect = mock_get_side_effect

        response = client.post("/order", params={"distance_km": 10})

        assert response.status_code == 404
        assert response.json()["detail"] == "На жаль, зараз немає вільних водіїв"
        import xmlrunner

if __name__ == '__main__':
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)