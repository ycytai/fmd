import requests


class ApiBase:
    @classmethod
    def _get_data(cls, url: str, **kwargs) -> list[dict] | dict | str:
        res = requests.get(url, params=kwargs)
        data = res.json()
        if res.status_code != 200:
            return data.get('msg')
        return data.get('data')
