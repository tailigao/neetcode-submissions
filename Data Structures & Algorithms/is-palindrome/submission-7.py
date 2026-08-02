class Solution:
    def isPalindrome(self, s: str) -> bool:
        # preprocessing
        lowercase = s.lower() #to lowercase
        alphanumerical = []
        for char in lowercase:
            if char.isalnum() == True:
                alphanumerical.append(char) #to alphanumerical only
        text = ''.join(alphanumerical) #to string
        
        # palindrome?
        left = 0
        right = len(text) - 1

        while left < right:
            if text[left] != text[right]:
                return False
            left += 1
            right -= 1

        return True
        


            
        