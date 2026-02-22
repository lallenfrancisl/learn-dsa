package main

func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	letters := make(map[rune]int)
	for _, l := range s {
		letters[l] += 1
	}

	for _, l := range t {
		letters[l] -= 1
	}

	for _, count := range letters {
		if count != 0 {
			return false
		}
	}

	return true
}
