from typing import TypeVar, Union

T = TypeVar("T", int, float)


def selection_sort(nums: list[T]) -> list[T]:
    """This is type of sorting algorithm `selection sort` which runs in 
    `O(n2)` time complexity and `O(1)` space complexity.

    :Approach
    - We are using two loop method, Outer loop runs `(0 -> len(nums)-1)`,
        - `len(nums)-1)` we skiping the last element that will be redundant check,
            because will will cover last element in the inner loop to check the minimum.
    - We are maintaining the pointer to store the index of the minimum value of the list,
        we are updating this `min_idx` in inner loop.
    - Inner loop will run (i+1 -> len) and we will compair the the value of `min_idx` and the nums[j],
        and we will update  the `min_idx`.
    """

    for i in range(len(nums)-1):
        min_idx = i
        for j in range(i + 1, len(nums)):
            if nums[min_idx] > nums[j]:
                min_idx = j
            nums[min_idx], nums[i] = nums[i], nums[min_idx]

    return nums


if __name__ == "__main__":
    selection_sort([5, 6, 3, 27, 78, 98, 5])
