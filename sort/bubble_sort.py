def bubble_sort[T](nums: list[T]) -> list[T]:
    """Bubble sort is a sorting algorithm that repeatedly steps through the list,
    compares adjacent elements and swaps them if they are in the wrong order.
    - Outer loop runs from the end to beginning of the list
    - Inner loop compares adjacent elements from start up to i
    - If adjacent elements are in wrong order, swap them
    - After each outer loop iteration, the largest unsorted element bubbles to its position
    """

    for i in range(len(nums) - 1, 0, -1):
        for j in range(0, i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    print(nums)
    return nums


bubble_sort([5, 4, 65, 54, 89, 2, 3, 0])
