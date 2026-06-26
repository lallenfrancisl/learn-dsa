import inspect
import importlib.util
from pathlib import Path
from typing import Any


TestCase = tuple[tuple[Any, ...], Any]
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"


INPUTS: dict[str, list[TestCase]] = {
    "217_contains_duplicate.py": [
        (([1, 2, 3, 1],), True),
        (([1, 2, 3, 4],), False),
    ],
    "242_valid_anagram.py": [
        (("anagram", "nagaram"), True),
        (("rat", "car"), False),
        (("aacc", "ccac"), False),
    ],
    "1_two_sum.py": [
        (([2, 7, 11, 15], 9), [0, 1]),
        (([3, 2, 4], 6), [1, 2]),
        (([3, 3], 6), [0, 1]),
    ],
    "49_group_anagrams.py": [
        (
            (["eat", "tea", "tan", "ate", "nat", "bat"],),
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ),
    ],
    "347_top_k_frequent_elements.py": [
        (([1, 1, 1, 2, 2, 3], 2), [1, 2]),
        (([1], 1), [1]),
        (([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2), [1, 2]),
    ],
    "238_product_of_array_except_self.py": [
        (([1, 2, 3, 4],), [24, 12, 8, 6]),
        # (([-1, 1, 0, -3, 3],), [0, 0, 9, 0, 0]),
    ],
    "128_longest_consecutive_sequence.py": [
        (([100, 4, 200, 1, 3, 2],), 4),
        (([0, 3, 7, 2, 5, 8, 4, 6, 0, 1],), 9),
        (([1, 0, 1, 2],), 3),
    ],
    "125_valid_palindrome.py": [
        (("A man, a plan, a canal: Panama",), True),
        (("race a car",), False),
        ((" ",), True),
    ],
    "15_3sum.py": [
        (([-1, 0, 1, 2, -1, -4],), [[-1, -1, 2], [-1, 0, 1]]),
        (([0, 1, 1],), []),
        (([0, 0, 0],), [[0, 0, 0]]),
        (([1, 2, 0, 1, 0, 0, 0, 0],), [[0, 0, 0]]),
    ],
    "11_container_with_most_water.py": [
        (([1, 8, 6, 2, 5, 4, 8, 3, 7],), 49),
        (([1, 1],), 1),
    ],
}


def _load_module(path: Path) -> Any:
    module_name = f"neetcode_150_{path.stem}"
    spec = importlib.util.spec_from_file_location(module_name, path)

    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load {path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module


def _solution_method(solution: Any) -> tuple[str, Any]:
    methods = [
        (name, method)
        for name, method in inspect.getmembers(solution, predicate=inspect.ismethod)
        if not name.startswith("_")
    ]

    if len(methods) != 1:
        raise ValueError(
            f"Expected exactly one public Solution method, found {len(methods)}"
        )

    return methods[0]


def _matches_expected(result: Any, expected: Any) -> bool:
    if isinstance(expected, list) and all(isinstance(item, list) for item in expected):
        if not isinstance(result, list) or not all(
            isinstance(item, list) for item in result
        ):
            return False

        normalized_result = sorted(sorted(group) for group in result)
        normalized_expected = sorted(sorted(group) for group in expected)

        return normalized_result == normalized_expected

    return result == expected


def run() -> None:
    folder = Path(__file__).parent
    for path in sorted(folder.glob("*.py")):
        if path.name == Path(__file__).name or path.name.startswith("_"):
            continue

        module = _load_module(path)
        test_cases = INPUTS.get(path.name)

        if test_cases is None:
            print(f"{path.name}: skipped, no inputs configured")
            continue

        for args, expected in test_cases:
            solution = module.Solution()
            method_name, method = _solution_method(solution)
            result = method(*args)
            status = (
                f"{GREEN}PASS{RESET}"
                if _matches_expected(result, expected)
                else f"{RED}FAIL{RESET}"
            )

            print(
                f"{path.name}: {method_name}{args!r} -> {result!r}; "
                f"expected {expected!r} [{status}]"
            )


if __name__ == "__main__":
    run()
