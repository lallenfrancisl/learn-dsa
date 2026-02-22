package main

func groupAnagrams(strs []string) [][]string {
	res := make(map[[26]int][]string)

	for _, str := range strs {
		count := [26]int{}

		for _, c := range str {
			count[c-'a'] += 1
		}

		res[count] = append(res[count], str)
	}

	result := make([][]string, 0)
	for _, group := range res {
		result = append(result, group)
	}

	return result
}
