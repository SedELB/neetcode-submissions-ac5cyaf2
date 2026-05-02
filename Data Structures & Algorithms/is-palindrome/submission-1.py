class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_string = "".join(char for char in s if char.isalnum()).lower()
    
        # for O(1) space (in-place) im gonna use two pointers
        # 0P
        left = 0
        right = len(clean_string) - 1

        while left < right:
            if clean_string[left] == clean_string[right]:
                left += 1
                right -= 1
            else:
                return False
        
        return True


