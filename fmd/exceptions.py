class RequestError(Exception):
    def __init__(self, status_code: int, msg: str) -> None:
        self.status_code = status_code
        self.msg = msg

    def __str__(self) -> str:
        return f'status code: {self.status_code}. {self.msg}'
