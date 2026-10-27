import unittest
from unittest.mock import patch

import app as application


class ThreeTierAppTests(unittest.TestCase):

    def setUp(self):
        application.app.config["TESTING"] = True
        self.client = application.app.test_client()

    @patch("app.check_redis", return_value=True)
    @patch("app.check_postgres", return_value=True)
    def test_health_all_services_connected(self, mock_postgres, mock_redis):
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {
            "application": "healthy",
            "postgresql": "connected",
            "redis": "connected",
        })

    @patch("app.check_redis", return_value=False)
    @patch("app.check_postgres", return_value=True)
    def test_health_when_redis_disconnected(self, mock_postgres, mock_redis):
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {
            "application": "degraded",
            "postgresql": "connected",
            "redis": "disconnected",
        })

    @patch("app.check_redis", return_value=False)
    @patch("app.check_postgres", return_value=False)
    def test_health_when_both_services_disconnected(
        self, mock_postgres, mock_redis
    ):
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {
            "application": "degraded",
            "postgresql": "disconnected",
            "redis": "disconnected",
        })

    @patch("app.redis_client.get", return_value="Hello from Redis")
    @patch("app.redis_client.set")
    def test_redis_route(self, mock_set, mock_get):
        response = self.client.get("/redis")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hello from Redis", response.data)
        mock_set.assert_called_once_with("message", "Hello from Redis")

    @patch("app.check_redis", return_value=True)
    @patch("app.check_postgres", return_value=True)
    def test_home_page(self, mock_postgres, mock_redis):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
