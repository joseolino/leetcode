""" 9. Palindrome Number
Level: Easy

Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:

-231 <= x <= 231 - 1

Follow up: Could you solve it without converting the integer to a string? """

import math


class Solution:
    def get_digit(self, number: int, n: int) -> int:
        return number // 10 ** n % 10

    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False
        elif (x == 0):
            return True
        digits = int(math.log10(x)) + 1
        half = int(digits / 2)
        for i in range(half):
            if (self.get_digit(x, i) != self.get_digit(x, (digits - i - 1))):
                return False
        return True


s = Solution()
print(s.isPalindrome(121))