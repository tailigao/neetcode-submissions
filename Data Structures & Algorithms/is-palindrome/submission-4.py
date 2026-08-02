class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = ""
        lower = s.lower()
        for char in lower:
            if char.isalpha() == True or char.isnumeric() == True:    
                text = text + char
        print(text)
        reversed_text = ""
        for char in text:
            reversed_text = char + reversed_text

        print(reversed_text)
        if reversed_text == text:
            return True
    
        else: 
            return False