class Solution:
    def myAtoi(self, s: str) -> int:
        int_limit = 2 ** 31
        max_limit = int_limit - 1
        min_limit = -int_limit
        result = 0
        signed = False
        if len(s) < 1:
            return 0
        i = 0
        while i < len(s) and s[i] == " ":
            i+= 1
        if i == len(s):
            return 0
        elif s[i] == "-":
            signed = True
            i += 1
        elif s[i] == "+":
            i += 1
        while i < len(s):
            if (s[i] <= "9" and s[i] >= "0"):
                result = result * 10 + int(s[i])
            else:
                break
            i += 1
        result = -result if signed else result
        if result > max_limit:
            result = max_limit
        elif result < min_limit:
            result = min_limit
        return result

s = Solution()

print(s.myAtoi("     +004500"))