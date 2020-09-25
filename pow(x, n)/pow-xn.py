class Solution:
    def myPow(self, x: float, n: int) -> float:
        total = 1
        print(abs(-2))
        if(n > 0):
            for i in range(0, n):
                total = total * x
            return total
        else:
            for i in range(0, abs(n)):
                total = total / x
            return total
        
