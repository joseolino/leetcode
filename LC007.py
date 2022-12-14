class Solution:
    def reverse(self, x: int) -> int:
        limit_int = 2 ** 31
        max_int = limit_int - 1
        min_int = -1 * limit_int
        signal = 1 if x > 0 else -1
        x = x * signal
        s = str(x)[::-1]
        result = int(s) * signal
        return result if (result <= max_int and result >= min_int) else 0