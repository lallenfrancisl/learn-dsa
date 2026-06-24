import inspect
import importlib.util
from pathlib import Path
from typing import Any


TestCase = tuple[tuple[Any, ...], Any]


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
            status = "PASS" if result == expected else "FAIL"

            print(
                f"{path.name}: {method_name}{args!r} -> {result!r}; "
                f"expected {expected!r} [{status}]"
            )


if __name__ == "__main__":
    run()
