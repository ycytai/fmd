from unittest.mock import MagicMock

import pytest
import requests

from fmd.backend import RequestsBackend


class TestRequestsBackend:

    @pytest.fixture(autouse=True)
    def setUp(self):
        self.backend = RequestsBackend()
        self.url = 'http://example.com'
        self.method = 'get'
        yield

    def test_send_request_success(self, mock_request) -> None:
        mock_response = MagicMock(spec=requests.Response)
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        response = self.backend.send_request(method=self.method, url=self.url)

        mock_request.assert_called_once_with(
            method=self.method,
            url=self.url,
            params=None,
            timeout=None,
            json=None,
        )
        assert response.status_code == 200

    def test_send_request_with_params(self, mock_request) -> None:
        mock_response = MagicMock(spec=requests.Response)
        mock_request.return_value = mock_response
        params = {'param1': 'value1'}

        self.backend.send_request(method=self.method, url=self.url, params=params)

        mock_request.assert_called_once_with(
            method=self.method,
            url=self.url,
            params=params,
            timeout=None,
            json=None,
        )

    def test_send_request_with_json(self, mock_request) -> None:
        mock_response = MagicMock(spec=requests.Response)
        mock_request.return_value = mock_response
        json_data = {'key': 'value'}

        self.backend.send_request(method=self.method, url=self.url, json=json_data)

        mock_request.assert_called_once_with(
            method=self.method,
            url=self.url,
            params=None,
            timeout=None,
            json=json_data,
        )

    def test_send_request_with_timeout(self, mock_request) -> None:
        mock_response = MagicMock(spec=requests.Response)
        mock_request.return_value = mock_response
        timeout = 5.0

        self.backend.send_request(method=self.method, url=self.url, timeout=timeout)

        mock_request.assert_called_once_with(
            method=self.method,
            url=self.url,
            params=None,
            timeout=timeout,
            json=None,
        )
