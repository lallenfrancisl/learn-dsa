package main

func productExceptSelf(nums []int) []int {
	products := make([]int, len(nums))

	product := 1
	for i := range nums {
		products[i] = product
		product = product * nums[i]
	}

	product = 1
	for i := len(nums) - 1; i >= 0; i-- {
		products[i] = product * products[i]
		product = product * nums[i]
	}

	return products
}
