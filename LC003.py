class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        i = 0
        max_streak = 0
        streak = 0
        while i < len(s):
            if(s[i] in hashmap.keys()):
                max_streak = streak if streak > max_streak else max_streak
                i = hashmap[s[i]] + 1
                hashmap = {}
                streak = 0
            else:
                hashmap[s[i]] = i
                i += 1
                streak += 1
        max_streak = streak if streak > max_streak else max_streak
        return max_streak


s = Solution()

print(s.lengthOfLongestSubstring("aab"))