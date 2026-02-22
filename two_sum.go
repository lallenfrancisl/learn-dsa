package main

func twoSum(nums []int, target int) []int {
	lookup := make(map[int]int)
	for i, num := range nums {
		diff := target - num
		if index, found := lookup[diff]; found {
			return []int{index, i}
		}

		lookup[num] = i
	}

	return []int{}
}
