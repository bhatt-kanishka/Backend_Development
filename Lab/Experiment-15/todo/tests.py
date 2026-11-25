from django.test import SimpleTestCase
from unittest.mock import Mock, patch
import requests

from .utils import get_external_data


class ExternalAPITests(SimpleTestCase):

    @patch("todo.utils.requests.get")
    def test_successful_api_response(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {
            "id": 1,
            "title": "Test post",
        }
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        result = get_external_data(1)

        self.assertEqual(result["data"]["id"], 1)
        self.assertIsNone(result["error"])
        mock_get.assert_called_once_with(
            "https://jsonplaceholder.typicode.com/posts/1",
            timeout=5,
        )

    @patch("todo.utils.requests.get")
    def test_api_timeout(self, mock_get):
        mock_get.side_effect = requests.Timeout

        result = get_external_data(1)

        self.assertIsNone(result["data"])
        self.assertEqual(
            result["error"],
            "External service timed out",
        )

    @patch("todo.utils.requests.get")
    def test_api_request_failure(self, mock_get):
        mock_get.side_effect = requests.ConnectionError

        result = get_external_data(1)

        self.assertIsNone(result["data"])
        self.assertEqual(
            result["error"],
            "External service is unavailable",
        )
