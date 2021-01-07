class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean up data
        s = ''.join(filter(str.isalnum, s)) 
        s = s.lower()
        # compare front and back letters iteratively
        for i in range(0, int(len(s)/2)):
            if(s[i] != s[len(s) - i - 1]):
                return False
        return True
                
        
