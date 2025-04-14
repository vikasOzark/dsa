from typing import TypeVar, List
T = TypeVar("T", int, float)


def merge(nums: List[int], low: int, mid: int, high: int):
    temp_list: list[int] = []

    left: int = low
    right: int = mid + 1

    while left <= mid and right <= high:
        if nums[left] <= nums[right]:
            temp_list.append(nums[left])
            left += 1
        else:
            temp_list.append(nums[right])
            right += 1

    while left <= mid:
        temp_list.append(nums[left])
        left += 1

    while right <= high:
        temp_list.append(nums[right])
        right += 1

    for i, val in enumerate(temp_list):
        nums[low + i] = val  # Correctly copying back to original array


def merge_sort(nums: List[int], low: int, high: int):
    if low >= high:
        return

    mid = (low + high) // 2

    merge_sort(nums, low, mid)
    merge_sort(nums, mid + 1, high)
    merge(nums, low, mid, high)


nums = [5, 2, 3, 1]
low = 0
high = len(nums) - 1  # Fixing the range

merge_sort(nums, low=low, high=high)
print(nums)  # Output: [1, 2, 3, 5]
