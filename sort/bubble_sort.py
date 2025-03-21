def bubble_sort[T](nums: list[T]) -> list[T]:
    for i in range(len(nums) - 1, 0, -1):
        for j in range(0, i - 1):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

    print(nums)
    return nums


bubble_sort([5, 2, 3])
