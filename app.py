"""フェボナッチ数列を返すAPI"""

from flask import Flask, request, jsonify

from utils.fibonacci import fibonacci
from utils.exceptions import (
    InvalidInputException,
    MissingParameterException,
    create_error_response,
)


HTTP_OK = 200


app = Flask(__name__)

# ===================== Error Handling ===================== #


@app.errorhandler(InvalidInputException)
def handle_invalid_input_exception(error):
    """
    invalid inputのエラーを処理する

    arg:
        error: InvalidInputException

    return:
        response: json
        status_code: int
    """

    response = create_error_response(error)

    return response, error.status_code


@app.errorhandler(MissingParameterException)
def handle_missing_parameter_exception(error):
    """
    パラメータを指定していない場合のエラーを処理する

    arg:
        error: MissingParameterException

    return:
        response: json
        status_code: int
    """

    response = create_error_response(error)

    return response, error.status_code


# ===================== API ===================== #


@app.route("/fib", methods=["GET"])
def get_fibonacci():
    """
    n番目のフェボナッチ数列を返す

    query parameter:
        n: int (1以上の整数)

    return:
        result: int (n番目のフェボナッチ数列)
    """
    n = request.args.get("n")

    if not n:  # nがない場合はエラーを返す
        raise MissingParameterException(parameter="n")
    elif not n.isdigit():  # 数字でない場合はエラーを返す
        raise InvalidInputException(
            message="Invalid input. n must be a positive integer."
        )

    result = fibonacci(int(n))

    return jsonify({"result": result}), HTTP_OK


if __name__ == "__main__":
    app.run(debug=True)
