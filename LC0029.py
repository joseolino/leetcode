class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if divisor == 0:
            raise ValueError("Cannot divide by 0")
        sign = True if (dividend < 0) ^ (divisor < 0) else False
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0
        while dividend >= divisor:
            shift = 0
            while dividend >= (divisor << shift):
                shift += 1
            result += 1 << (shift - 1)
            dividend -= divisor << (shift - 1)
        result = -result if sign else result
        if result < -2147483648:
            return -2147483648
        elif result > 2147483647:
            return 2147483647
        else:
            return result

s = Solution()

print(s.divide(10, 3))