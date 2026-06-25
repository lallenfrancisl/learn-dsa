from typing import Dict, List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts: Dict[int, int] = {}
        for i in nums:
            if i not in counts:
                counts[i] = 0

            counts[i] += 1

        sorted_bucket: List[List[int]] = [[] for _ in nums]
        for key, value in counts.items():
            sorted_bucket[value - 1].append(key)

        result: List[int] = []
        for el in reversed(sorted_bucket):
            if len(el):
                result.extend(el)

            if len(result) == k:
                return result

        return []
