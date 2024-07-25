from datetime import date

import pytest

from fmd.client import FmdApi


@pytest.fixture
def mock_get(mocker):
    yield mocker.patch('requests.get')


@pytest.fixture
def mock_get_data(mocker):
    yield mocker.patch.object(FmdApi, '_get_data')


@pytest.fixture(
    params=[
        pytest.param((2330, None, None), id='without date range'),
        pytest.param((2330, '2023-01-01', '2023-12-31'), id='with string date range'),
        pytest.param((2330, date(2023, 1, 1), date(2023, 12, 31)), id='with object date range'),
    ]
)
def mock_get_daily_data_params(request):
    yield request.param
