def list_divide(numbers, divide=2):
    """Return how many items in numbers are evenly divisible by divide."""
    if divide == 0:
        return 0
    return sum(1 for n in numbers if n % divide == 0)


class ListDivideException(Exception):
    """Custom exception for list_divide test failures"""
    pass


def test_list_divide():
    """Run tests on list_divide and raise exception if any fail"""
    tests = [
        (list_divide([1, 2, 3, 4, 5]), 2),
        (list_divide([2, 4, 6, 8, 10]), 5),
        (list_divide([30, 54, 63, 98, 100], divide=10), 2),
        (list_divide([]), 0),
        (list_divide([1, 2, 3, 4, 5], 1), 5),
    ]

    for idx, (got, expected) in enumerate(tests, start=1):
        if got != expected:
            raise ListDivideException(f"Test {idx} failed. Got {got}, expected {expected}")


if __name__ == "__main__":
    test_list_divide()
    print("All tests passed")