"""フェボナッチ数列を返す関数"""

from utils.exceptions import InvalidInputException


def fibonacci(n):
    """
    フェボナッチ数列を返す

    args:
        n: int (1以上の整数)
    """
    if n <= 0 or not isinstance(n, int):  # 正の整数でない場合はエラーを返す
        raise InvalidInputException(
            message="Invalid input. n must be a positive integer."
        )
    elif n <= 2:  # 1, 2の場合は1を返す
        return 1
    else:
        fib_prev, fib_curr = 1, 1
        for _ in range(n - 2):
            fib_next = fib_prev + fib_curr
            fib_prev, fib_curr = fib_curr, fib_next
        return fib_curr
