from collections import Counter
from typing import Optional, Set


# def get_perms(s: str) -> Optional[Set[str]]:
#     if s is None:
#         return None
#
#     permutations = set()  # noqa
#
#     r_get_perms('', s, permutations)
#
#     return permutations
#
#
# def r_get_perms(prefix: str, remainder: str, permutations: Set[str]) -> None:
#     if not remainder:  # Base case
#         if prefix not in permutations:
#             permutations.add(prefix)
#
#     for c in remainder:
#         r_get_perms(prefix + c, remainder.replace(c, '', 1), permutations)


# def get_perms(s: str) -> Optional[List[str]]:
#     if s is None:
#         return None
#
#     permutations = []  # noqa
#
#     perms_cache = set()  # type: Set[Tuple[str, str]]
#
#     r_get_perms('', s, permutations, perms_cache)
#
#     return permutations
#
#
# def r_get_perms(prefix: str, remainder: str, permutations: List[str], perms_cache: Set[Tuple[str, str]])\
#         -> None:
#     if (prefix, remainder) in perms_cache:
#         return None
#
#     if not remainder:  # Base case
#         permutations.append(prefix)
#
#     for c in remainder:
#         r_get_perms(prefix + c, remainder.replace(c, '', 1), permutations, perms_cache)
#
#     perms_cache.add((prefix, remainder))

def get_perms(s: str) -> Optional[Set[str]]:
    if s is None:
        return None

    permutations = set()  # noqa

    freq_map = Counter(s)

    r_get_perms(freq_map, '', len(s), permutations)

    return permutations


def r_get_perms(freq_map: Counter, prefix: str, remaining, permutations: Set[str]) -> None:
    if not remaining:  # Base case
        permutations.add(prefix)
        return None

    for c in freq_map:
        count = freq_map[c]
        if count:
            freq_map[c] = count - 1
            r_get_perms(freq_map, prefix + c, remaining - 1, permutations)
            freq_map[c] = count


if __name__ == "__main__":
    perms = get_perms("aab")
    print(len(perms))
    print(perms)
