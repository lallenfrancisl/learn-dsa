class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res: list[list[int]] = []

        self.dfs(candidates, res, target, 0, [], 0)

        return res

    def dfs(
        self,
        candidates: list[int],
        res: list[list[int]],
        target: int,
        i: int,
        cur: list[int],
        total: int,
    ):
        if total == target:
            res.append(cur.copy())

            return

        if i >= len(candidates) or total > target:
            return

        cur.append(candidates[i])
        self.dfs(
            candidates,
            res,
            target,
            i,
            cur,
            total + candidates[i],
        )

        cur.pop()
        self.dfs(
            candidates,
            res,
            target,
            i + 1,
            cur,
            total,
        )
