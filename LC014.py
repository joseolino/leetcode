class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        min_len = 201
        output = ""
        for string in strs:
            if len(string) < min_len:
                min_len = len(string)
        for i in range(min_len):
            c = strs[0][i]
            equal = True
            for string in strs:
                if(string[i] != c):
                    equal = False
                    break
            if equal:
                output += c
            else:
                break
        return output

s = Solution()

strs = ["flower","flow","flight"]

print(s.longestCommonPrefix(strs))