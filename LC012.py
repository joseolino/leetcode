class Solution:

    def prepare(self, s: str) -> str:
        s = s.replace("DCCCC", "CM")
        s = s.replace("CCCC", "CD")
        s = s.replace("LXXXX", "XC")
        s = s.replace("XXXX", "XL")
        s = s.replace("VIIII", "IX")
        s = s.replace("IIII", "IV")
        return s

    def intToRoman(self, num: int) -> str:
        result = ""
        table = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        for i, (roman, dec) in enumerate(table.items()):
            while num // dec > 0:
                result += roman
                num -= dec
        return self.prepare(result)

s = Solution()

print (s.intToRoman(3999))