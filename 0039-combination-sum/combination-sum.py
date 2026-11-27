from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(start: int, remaining: int, path: List[int]) -> None:
            if remaining == 0:
                res.append(path.copy())
                return

            for i in range(start, len(candidates)):
                val = candidates[i]
                if val > remaining:
                    break

                path.append(val)
                backtrack(i, remaining - val, path)
                path.pop()

        backtrack(0, target, [])
        return res