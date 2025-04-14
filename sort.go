package main

import (
	"fmt"
	"slices"
)

func main() {
	nums := []int{5, 2, 3, 10, 1}
	fmt.Println("Original:", nums)
	// largest_element_2(nums)
	// largest_element(nums)
	kth_largest(nums, 2)
	// fmt.Println(nums[len(nums)-1])
}

func largest_element_ptr(nums []int) int {

	max := 0
	for i := 1; i < len(nums); i++ {
		if nums[i] > nums[max] {
			max = i
		}
	}
	fmt.Println(nums[max])
	return nums[max]
}

func largest_element_2(nums []int) {
	n := len(nums)
	for i := 0; i <= n; i++ {
		for j := i; j < n-1; j++ {
			if nums[j] > nums[j+1] {
				nums[j], nums[j+1] = nums[j+1], nums[j]
			}
		}
	}

	fmt.Println(nums[len(nums)-1])
}

func largest_element_recursive(nums []int, n int) {
	if n == 1 {
		return
	}

	for i := range n - 1 {
		if nums[i] > nums[i+1] {
			nums[i], nums[i+1] = nums[i+1], nums[i]
		}
	}

	largest_element_recursive(nums, n-1)
}

func kth_largest(nums []int, k int) int {
	max := 0
	for j := range k {
		counter := j + 1
		for i := 0; i < len(nums)-1; i++ {
			if nums[i] > nums[max] {
				max = i
			}
		}
		if counter == k-1 {
			nums = slices.Delete(nums, max, max+1)
		}
	}
	print(nums[max])
	return nums[max]
}
