"""
UMass ECE 241 - Advanced Programming
Homework #4     Fall 2021
question1.py - DP planks with turtle
"""


### Longest Palindrome
test_cases = [
 "a", "abaab", "racecar", "bullet", "rarfile",
 "computer", "windows", "saippuakivikauppias",
 "aaaaaaaaaaaaaaaaadaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
 "kkkkkkkkkkkkkkkkkkkkkkdldkkkkkkkkkkkkkkkkkkkkkk",
 "ddddddddddddddddddddddddddddddddddddddddddddddddddks"
]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0       # Start position of longest palindrome 
        end = 0         # End position of longest palindrome

        for i in range(0, len(s)):
            # Palindome can be centered around 1 character or 2 characteres.
            # example aba  -> center is a
            #         abba -> center is bb
            # Try both methods and see which one gives the longer palindome.

            l1 = self.expand_around(s, i, i)
            l2 = 0
            if i + 1 < len(s):
                l2 = self.expand_around(s, i, i + 1)

            if l1 > l2:
                # if longer than the current longest palindrome
                if l1 > (end - start) + 1:
                    # record odd
                    start = i - (l1 // 2)
                    end = i + (l1 // 2)
            else:
                if l2 > (end - start) + 1:
                    start = i - ((l2 // 2) - 1)
                    end = i + (l2 // 2)
            i += 1
            pass
                
        return s[start : end+1]
    
    def expand_around(self, s, left, right):
        if s[left] != s[right]:
            return 0


        while (left >= 0 and right < len(s) and s[left] == s[right]):
            tempL = left
            tempR = right

            left -= 1
            right += 1

        return (tempR - tempL) + 1

        pass
        
        
        
if __name__ == "__main__":
    solution = Solution()
    
    for test_case in test_cases:
        print(solution.longestPalindrome(test_case))
    