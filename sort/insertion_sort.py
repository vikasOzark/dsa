from typing import TypeVar

T = TypeVar('T', int, float)


def insertion_sort(nums: list[T]) -> list[T]:
    for i in range(1, len(nums)):
        index = i
        while nums[index - 1] > nums[index] and index > 0:
            nums[index-1], nums[index] = nums[index], nums[index-1]
            index -= 1
    return nums


insertion_sort([1, 0, 5, 63, 2, 4, 65, 0])
