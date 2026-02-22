package main

func containsDuplicate(nums []int) bool {
	lookup := make(map[int]bool)
	for _, num := range nums {
		if _, found := lookup[num]; found {
			return true
		}

		lookup[num] = true
	}

	return false
}
