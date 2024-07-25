from unittest.mock import MagicMock

from fmd.base import ApiBase


class TestApiBase:

    def test_get_data_success(self, mock_get):
        params = {'param1': 'value1'}
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'data': [{'key': 'value'}]}
        mock_get.return_value = mock_response

        result = ApiBase._get_data('https://api.example.com', **params)

        assert result == [{'key': 'value'}]
        mock_get.assert_called_once_with('https://api.example.com', params=params)

    def test_get_data_error(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.json.return_value = {'msg': 'Bad Request'}
        mock_get.return_value = mock_response

        result = ApiBase._get_data('https://api.example.com')

        assert result == 'Bad Request'
        mock_get.assert_called_once_with('https://api.example.com', params={})

    def test_get_data_with_params(self, mock_get):
        params = {'param1': 'value1', 'param2': 'value2'}
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'data': {'key': 'value'}}
        mock_get.return_value = mock_response

        result = ApiBase._get_data('https://api.example.com', **params)

        assert result == {'key': 'value'}
        mock_get.assert_called_once_with('https://api.example.com', params=params)
