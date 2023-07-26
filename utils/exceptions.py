""" Custom exceptions for the API."""

from flask import jsonify

HTTP_BAD_REQUEST = 400


class MissingParameterException(Exception):
    """パラメータが未指定の場合の例外"""

    def __init__(self, parameter):
        self.parameter = parameter
        self.message = f"Missing query parameter '{parameter}'. Please provide '{parameter}' as a positive integer."
        self.status_code = HTTP_BAD_REQUEST
        super().__init__(self.message)


class InvalidInputException(Exception):
    """パラメータが不正な場合の例外"""

    def __init__(self, message="Invalid input.", status_code=HTTP_BAD_REQUEST):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


def create_error_response(error):
    """
    エラー用のレスポンスを作成する

    arg:
        error: Exception

    return:
        response: json
    """

    response = jsonify({"status": error.status_code, "message": error.message})

    # 整形
    response.json_dumps_args = {"indent": 2}

    return response
