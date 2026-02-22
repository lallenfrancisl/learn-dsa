package main

import "fmt"

func main() {
	fmt.Printf(
		"containsDuplicates: %v\n", containsDuplicate([]int{1, 3, 2, 1}),
	)
	fmt.Printf(
		"isAnagram: %v\n", isAnagram("anagram", "nagaram"),
	)
	fmt.Printf(
		"twoSum: %v\n", twoSum([]int{3, 2, 4}, 6),
	)
	fmt.Printf(
		"groupAnagram: %v\n",
		groupAnagrams([]string{"eat", "tea", "tan", "ate", "nat", "bat"}),
	)
	fmt.Printf(
		"topKFrequent: %v\n",
		topKFrequent([]int{1, 2, 1, 2, 1, 2, 3, 1, 3, 2}, 2),
	)
}
