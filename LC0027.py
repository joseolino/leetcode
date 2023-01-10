from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        result = 0
        skip = 0
        for i in range(len(nums)):
            if nums[i] == val:
                skip += 1
            else:
                nums[i - skip] = nums[i]
                result += 1
        return result

s = Solution()

list = [1, 2, 3, 4, 4, 6]

print(s.removeElement(list, 4))

print(list)