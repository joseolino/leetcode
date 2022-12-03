from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, n in enumerate(nums):
            if((target - n) not in map.keys()):
                map[n] = i
            else:
                return [i, map[target - n]]
        return []

s = Solution()

print(s.twoSum([1, 2, 3, 4, 7], 6))