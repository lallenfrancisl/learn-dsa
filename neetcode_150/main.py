import inspect
import importlib.util
from copy import deepcopy
from pathlib import Path
from typing import Any

from list_node import ListNode, to_list_node


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
    "encode_and_decode_strings.py": [
        ((["Hello", "World"],), ["Hello", "World"]),
    ],
    "20_valid_parentheses.py": [
        (("()",), True),
        (("()[]{}",), True),
        (("(]",), False),
        (("([])",), True),
        (("([)]",), False),
    ],
    "153_find_minimum_in_rotated_sorted_array.py": [
        (([3, 4, 5, 1, 2],), 1),
        (([4, 5, 6, 7, 0, 1, 2],), 0),
        (([11, 13, 15, 17],), 11),
    ],
    "33_search_in_rotated_sorted_array.py": [
        (([4, 5, 6, 7, 0, 1, 2], 0), 4),
        (([4, 5, 6, 7, 0, 1, 2], 3), -1),
        (([1], 0), -1),
        (([1], 1), 0),
        (([3, 5, 1], 3), 0),
    ],
    "121_best_time_to_buy_and_sell_stock.py": [
        (([7, 1, 5, 3, 6, 4],), 5),
        (([7, 6, 4, 3, 1],), 0),
    ],
    "3_longest_substring_without_repeating_characters.py": [
        (("abcabcbb",), 3),
        (("bbbbb",), 1),
        (("pwwkew",), 3),
        (("dvdf",), 3),
    ],
    "424_longest_repeating_character_replacement.py": [
        (("ABAB", 2), 4),
        (("AABABBA", 1), 4),
    ],
    "76_minimum_window_substring.py": [
        (("ADOBECODEBANC", "ABC"), "BANC"),
        (("a", "a"), "a"),
        (("a", "aa"), ""),
    ],
    "206_reverse_linked_list.py": [
        (
            (to_list_node([1, 2, 3, 4, 5]),),
            to_list_node([5, 4, 3, 2, 1]),
        )
    ],
    "21_merge_two_sorted_lists.py": [
        (
            (to_list_node([1, 2, 4]), to_list_node([1, 3, 4])),
            to_list_node([1, 1, 2, 3, 4, 4]),
        ),
        (
            (to_list_node([]), to_list_node([])),
            to_list_node([]),
        ),
        (
            (to_list_node([]), to_list_node([0])),
            to_list_node([0]),
        ),
    ],
    "143_reorder_list.py": [
        (
            (to_list_node([1, 2, 3, 4]),),
            to_list_node([1, 4, 2, 3]),
        ),
        (
            (to_list_node([1, 2, 3, 4, 5]),),
            to_list_node([1, 5, 2, 4, 3]),
        ),
    ],
    "19_remove_nth_node_from_end_of_list.py": [
        (
            (to_list_node([1, 2, 3, 4, 5]), 2),
            to_list_node([1, 2, 3, 5]),
        ),
        (
            (
                to_list_node(
                    [
                        1,
                    ]
                ),
                1,
            ),
            to_list_node([]),
        ),
    ],
    "23_merge_k_sorted_lists.py": [
        (
            (
                [
                    to_list_node([1, 4, 5]),
                    to_list_node([1, 3, 4]),
                    to_list_node([2, 6]),
                ],
            ),
            to_list_node([1, 1, 2, 3, 4, 4, 5, 6]),
        ),
        (
            ([],),
            to_list_node([]),
        ),
        (
            ([to_list_node([])],),
            to_list_node([]),
        ),
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


def _solution_methods(solution: Any) -> list[tuple[str, Any]]:
    methods = [
        (name, getattr(solution, name))
        for name, value in type(solution).__dict__.items()
        if not name.startswith("_") and inspect.isfunction(value)
    ]

    if len(methods) == 0:
        raise ValueError("Expected at least one public Solution method")

    variant_methods = [
        method
        for method in methods
        if method[0].lower().endswith(("recursive", "looped"))
    ]

    return variant_methods or [methods[0]]


def _solution_classes(module: Any) -> list[tuple[str, Any]]:
    classes = [
        (name, value)
        for name, value in module.__dict__.items()
        if inspect.isclass(value)
        and name.startswith("Solution")
        and name.lower().endswith(("recursive", "looped"))
    ]

    if len(classes) > 0:
        return classes

    if hasattr(module, "Solution"):
        return [("Solution", module.Solution)]

    raise AttributeError(f"{module.__name__} has no Solution class")


def _matches_expected(result: Any, expected: Any) -> bool:
    if isinstance(expected, ListNode):
        return isinstance(result, ListNode) and _matches_expected(
            result.to_list(), expected.to_list()
        )

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
            for solution_name, solution_class in _solution_classes(module):
                for method_name, _ in _solution_methods(solution_class()):
                    solution = solution_class()
                    method = getattr(solution, method_name)
                    method_args = deepcopy(args)
                    result = method(*method_args)
                    status = (
                        f"{GREEN}PASS{RESET}"
                        if _matches_expected(result, expected)
                        else f"{RED}FAIL{RESET}"
                    )

                    print(
                        f"{path.name}: {solution_name}.{method_name}{args!r} "
                        f"-> {result!r}; expected {expected!r} [{status}]"
                    )


if __name__ == "__main__":
    run()
