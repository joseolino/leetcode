class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        result = -1
        for i, c in enumerate(haystack[:(len(haystack) - len(needle) + 1)]):
            if haystack[i:i+len(needle)] == needle:
                return i
        return result

s = Solution()

print(s.strStr("a", "a"))