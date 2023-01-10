from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        found = False
        # 1st case: Looking for zero triplet
        if(len([x for x in nums if x == 0]) > 2):
            result.add((0, 0, 0))


        for index_pos, x in enumerate(nums):
            if x >= 0:
                found = True
                break
        if not found:
            return result
        i = 0
        while (i < index_pos):
            j = len(nums) - 1
            while (j >= index_pos):
                target = - (nums[i] + nums[j])
                if (target < nums[i] or target > nums[j]):
                    j -= 1
                    continue
                if (target >= 0):
                    k = index_pos
                    while(k < j and nums[k] <= target):
                        if(nums[k] == target):
                            result.add(tuple([nums[i],nums[k],nums[j]]))
                            break
                        else:
                            k += 1
                else:
                    k = index_pos - 1
                    while (k > i and nums[k] >= target):
                        if(nums[k] == target):
                            result.add(tuple([nums[i],nums[k],nums[j]]))
                            break
                        else:
                            k -= 1
                j -= 1
            i += 1

        return [[a,b,c] for (a,b,c) in result]

s = Solution()

print(s.threeSum([-2, -1, 0, 1, 1, 2]))