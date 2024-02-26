from typing import Dict

count = 0


def str_to_bool(s: str) -> bool:
    return s == '1'


def count_eval(expression: str, result: bool) -> int:  # noqa
    memo = {}  # type: Dict[str, int]
    return r_count_eval(expression, result, memo)


def r_count_eval(expression: str, result: bool, memo: Dict[str, int]) -> int:  # noqa
    global count
    count += 1

    if not expression:
        return 0
    elif len(expression) == 1:
        return 1 if str_to_bool(expression) == result else 0
    elif str(result) + expression in memo:
        return memo[str(result) + expression]

    ways = 0

    for i in range(1, len(expression), 2):
        o = expression[i]
        left = expression[:i]
        right = expression[i + 1:]
        left_true = r_count_eval(left, True, memo)
        left_false = r_count_eval(left, False, memo)
        right_true = r_count_eval(right, True, memo)
        right_false = r_count_eval(right, False, memo)
        total = (left_true + left_false) * (right_true + right_false)

        total_true = 0
        if o == '^':
            # required: one True and one False
            total_true = left_true * right_false + left_false * right_true
        elif o == '&':
            # required: two True
            total_true = left_true * right_true
        elif o == '|':
            # required: one True
            total_true = left_true * right_true + left_true * right_false + left_false * right_true

        subways = total_true if result else total - total_true
        ways += subways

    memo[str(result) + expression] = ways
    return ways


if __name__ == "__main__":
    expression = "0^0|1&1^1|0|1"
    # expression = '0|0|1'
    result = True

    print(count_eval(expression, result))
    print(count)
