import pytest


@pytest.fixture
def mock_request(mocker):
    yield mocker.patch('requests.Session.request')


@pytest.fixture
def mock_send_request(mocker):
    yield mocker.patch('fmd.backend.RequestsBackend.send_request')


@pytest.fixture
def mock_fa_send_request(mocker):
    yield mocker.patch('fmd.client.FmdApi.send_request')


@pytest.fixture
def mock_manager_get(mocker):
    yield mocker.patch('fmd.base.ManagerBase.get')
