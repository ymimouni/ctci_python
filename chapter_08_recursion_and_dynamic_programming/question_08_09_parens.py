def print_valid_parens(n: int) -> None:
    if n <= 0:
        return None

    r_print_valid_parens('', n, n)


def r_print_valid_parens(prefix: str, l_remaining: int, r_remaining: int) -> None:
    if not l_remaining and not r_remaining:
        print(prefix)
    elif l_remaining > r_remaining:
        return None
    else:
        if l_remaining:
            r_print_valid_parens(prefix + '(', l_remaining - 1, r_remaining)
        if r_remaining:
            r_print_valid_parens(prefix + ')', l_remaining, r_remaining - 1)


if __name__ == "__main__":
    print_valid_parens(3)
