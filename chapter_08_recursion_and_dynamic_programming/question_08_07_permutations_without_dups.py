from typing import List, Optional


def get_perms(s: str) -> Optional[List[str]]:
    if s is None:
        return None

    permutations = []  # noqa

    r_get_perms('', s, permutations)

    return permutations


def r_get_perms(prefix: str, remainder: str, permutations: List[str]) -> None:
    if not remainder:  # Base case
        permutations.append(prefix)

    for c in remainder:
        r_get_perms(prefix + c, remainder.replace(c, '', 1), permutations)


if __name__ == "__main__":
    perms = get_perms("abc")
    print(len(perms))
    print(perms)
