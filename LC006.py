class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ss = [[] for _ in range(numRows)]
        way = 1
        j = 0
        for c in s:
            ss[j].append(c);
            j += way
            if j == numRows - 1:
                way = -1
            elif j == 0:
                way = 1
        result = []
        for string in ss:
            result += string
        return "".join(result)

s = Solution()

print(s.convert("AB", 1))
