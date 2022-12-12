from typing import List

class Solution:

    def merge(self, nums1: List[int], nums2: List[int]) -> List[int]:
        merged = []
        i = 0
        j = 0
        k = 0
        while(i < len(nums1) + len(nums2) and j < len(nums1) and k < len(nums2)):
            if (nums1[j] < nums2[k]):
                merged.append(nums1[j])
                j += 1
            else:
                merged.append(nums2[k])
                k += 1
            i += 1
        while(j < len(nums1)):
            merged.append(nums1[j])
            j += 1
            i += 1
        while (k < len(nums2)):
            merged.append(nums2[k])
            k += 1
            i += 1
        return merged

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = self.merge(nums1, nums2)
        half = len(merged) // 2
        if(len(merged) % 2):
            return merged[half]
        else:
            return (merged[half - 1] + merged[half]) / 2

s = Solution()

print(s.findMedianSortedArrays([1,3], [2, 4]))