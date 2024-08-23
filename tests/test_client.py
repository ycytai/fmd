from unittest.mock import MagicMock

import pytest

from fmd import FmdApi
from fmd.exceptions import RequestError


class TestFmdApi:
    @pytest.fixture(autouse=True)
    def setUp(self):
        self.api = FmdApi()
        self.method = 'get'
        self.path = '/test'
        self.url = self.api._get_url(self.path)
        yield

    def test_send_request_success(self, mock_send_request) -> None:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'status': 'success', 'msg': 'ok', 'data': 'result'}
        mock_send_request.return_value = mock_response

        response = self.api.send_request(method=self.method, path=self.path)

        mock_send_request.assert_called_once_with(
            method=self.method, url=self.url, json=None, params=None, timeout=None
        )
        assert response == 'result'

    def test_send_request_with_params(self, mock_send_request) -> None:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'status': 'success', 'msg': 'ok', 'data': 'result'}
        mock_send_request.return_value = mock_response
        params = {'param1': 'value1'}

        response = self.api.send_request(method=self.method, path=self.path, params=params)

        mock_send_request.assert_called_once_with(
            method=self.method, url=self.url, json=None, params=params, timeout=None
        )
        assert response == 'result'

    def test_send_request_with_json(self, mock_send_request) -> None:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'status': 'success', 'msg': 'ok', 'data': 'result'}
        mock_send_request.return_value = mock_response
        json_data = {'key': 'value'}

        response = self.api.send_request(method=self.method, path=self.path, json=json_data)

        mock_send_request.assert_called_once_with(
            method=self.method, url=self.url, json=json_data, params=None, timeout=None
        )
        assert response == 'result'

    def test_send_request_with_timeout(self, mock_send_request) -> None:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'status': 'success', 'msg': 'ok', 'data': 'result'}
        mock_send_request.return_value = mock_response
        timeout = 5.0

        response = self.api.send_request(method=self.method, path=self.path, timeout=timeout)

        mock_send_request.assert_called_once_with(
            method=self.method, url=self.url, json=None, params=None, timeout=timeout
        )
        assert response == 'result'

    def test_send_request_retry(self, mock_send_request) -> None:
        mock_send_request.side_effect = [Exception('Connection error')] * 5 + [
            MagicMock(
                status_code=200, json=lambda: {'status': 'success', 'msg': 'ok', 'data': 'result'}
            )
        ]

        response = self.api.send_request(method=self.method, path=self.path, max_retries=10)

        assert response == 'result'
        assert mock_send_request.call_count == 6

    def test_send_request_failure(self, mock_send_request) -> None:
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.json.return_value = {'msg': 'error'}
        mock_send_request.return_value = mock_response

        with pytest.raises(RequestError):
            self.api.send_request(method=self.method, path=self.path)
