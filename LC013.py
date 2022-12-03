class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        lastDigit = ""
        for i, romanDigit in enumerate(s):
            nextDigit = ""
            if i + 1 < len(s):
                nextDigit = s[i + 1]
            if romanDigit not in "MDCLXVI":
                continue
            if romanDigit == "M" and lastDigit != "C":
                result += 1000
            elif romanDigit == "D" and lastDigit != "C":
                result += 500
            elif romanDigit == "C":
                if nextDigit == "M":
                    result += 900
                elif nextDigit == "D":
                    result += 400
                elif lastDigit != "X":
                    result += 100
            elif romanDigit == "L" and lastDigit != "X":
                result += 50
            elif romanDigit == "X":
                if nextDigit == "C":
                    result += 90
                elif nextDigit == "L":
                    result += 40
                elif lastDigit != "I":
                    result += 10
            elif romanDigit == "V" and lastDigit != "I":
                result += 5
            elif romanDigit == "I":
                if nextDigit == "X":
                    result += 9
                elif nextDigit == "V":
                    result += 4
                else:
                    result += 1
            lastDigit = romanDigit
        return result

number = "MMMCMLXXXIX"

sol = Solution()

print(sol.romanToInt(number))