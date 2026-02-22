package main

func topKFrequent(nums []int, k int) []int {
	counts := make(map[int]int)
	freq := make([][]int, len(nums)+1)

	for _, num := range nums {
		counts[num] += 1
	}

	for num, count := range counts {
		freq[count] = append(freq[count], num)
	}

	result := []int{}
	for i := len(freq) - 1; len(result) < k; i-- {
		for _, num := range freq[i] {
			result = append(result, num)

			if len(result) == k {
				return result
			}
		}
	}

	return result
}
