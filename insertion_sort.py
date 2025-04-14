from typing import List, TypeVar

T = TypeVar('T', int, float)


def insertion_sort(nums: List[T]) -> List[T]:
    """Sort a list in ascending order using the insertion sort algorithm.

    Args:
        nums (List[T]): List of numbers to sort

    Returns:
        List[T]: Sorted list in ascending order

    Example:
        >>> lst = [5, 2, 8, 1, 9]
        >>> insertion_sort(lst)
        [1, 2, 5, 8, 9]

    Time Complexity: O(n²) where n is length of list
    Space Complexity: O(1) as sorting is done in-place
    """

    if not nums:
        return nums

    for i in range(1, len(nums)):
        j = i
        print("j value : ", nums[j])
        while nums[j - 1] > nums[j] and j > 0:
            print(f"[j-1] -> {nums[j-1]} | [j] -> {nums[j]}")
            nums[j-1], nums[j] = nums[j], nums[j-1]
            j -= 1

    return nums


def main():
    # Test cases
    test_cases = [
        [100, 5, 9, 7, 8, 63],
        [],
        [1],
        [2, 1],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1]
    ]

    for arr in test_cases:
        original = arr.copy()
        sorted_arr = insertion_sort(arr)
        print(f"Original: {original}")
        print(f"Sorted  : {sorted_arr}\n")


if __name__ == "__main__":
    main()
