""" Custom exceptions for the API."""

HTTP_BAD_REQUEST = 400


class InvalidInputException(Exception):
    """パラメータが不正な場合の例外"""

    def __init__(self, message="Invalid input.", status_code=HTTP_BAD_REQUEST):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)
