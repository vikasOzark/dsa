from typing import TypeVar

T = TypeVar("T", int, float)


def merge(nums: list[T], *, low: int, mid: int, high: int) -> None:
    """Merges two sorted portions of the array into one sorted array.

    Think of it like shuffling two decks of sorted cards together:
    - You look at the top card of each deck
    - Take the smaller card and put it in the final deck
    - Repeat until all cards are used

    Args:
        nums: The array containing elements to merge
        low: Start index of first portion
        mid: End index of first portion
        high: End index of second portion
    """
    # Create temporary arrays for left and right portions
    left_half = nums[low:mid + 1]    # First portion: from low to mid
    right_half = nums[mid + 1:high]  # Second portion: from mid+1 to high

    left_index = right_index = 0  # Pointers for left and right
    main_arr_index = low  # Pointer for main array

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] <= right_half[right_index]:
            nums[main_arr_index] = left_half[left_index]
            left_index += 1
        else:
            nums[main_arr_index] = right_half[right_index]
            right_index += 1
        main_arr_index += 1

    while left_index < len(left_half):
        nums[main_arr_index] = left_half[left_index]
        left_index += 1
        main_arr_index += 1

    while right_index < len(right_half):
        nums[main_arr_index] = right_half[right_index]
        right_index += 1
        main_arr_index += 1


def merge_sort(nums: list[T], *, low: int, high: int) -> list[T]:
    if low >= high:  # Base case
        return nums
    mid = (low + high) // 2
    merge_sort(nums, low=low, high=mid)
    merge_sort(nums, low=mid + 1, high=high)

    merge(nums, low=low, mid=mid, high=high)
    return nums


if __name__ == "__main__":
    test_array = [5, 6, 2, 3]
    print(f"Original array: {test_array}")
    merge_sort(test_array, low=0, high=len(test_array))
    print(f"Sorted array: {test_array}")

    # # Initialize pointers
    # left_idx = 0       # Points to current element in left array
    # right_idx = 0      # Points to current element in right array
    # nums_idx = low     # Points to current position in original array

    # # Main merging loop - compare and place smaller element
    # while left_idx < len(left_half) and right_idx < len(right_half):
    #     if left_half[left_idx] <= right_half[right_idx]:
    #         nums[nums_idx] = left_half[left_idx]
    #         left_idx += 1
    #     else:
    #         nums[nums_idx] = right_half[right_idx]
    #         right_idx += 1
    #     nums_idx += 1

    # # If any elements are left in left_half, add them
    # while left_idx < len(left_half):
    #     nums[nums_idx] = left_half[left_idx]
    #     left_idx += 1
    #     nums_idx += 1

    # # If any elements are left in right_half, add them
    # while right_idx < len(right_half):
    #     nums[nums_idx] = right_half[right_idx]
    #     right_idx += 1
    #     nums_idx += 1

 # i love uh
