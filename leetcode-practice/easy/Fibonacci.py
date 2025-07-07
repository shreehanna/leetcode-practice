class Solution:
    def fib(self,n):
        if n==0:
            return 0
        elif n==1:
            return 1
        a,b=0,1
        for i in range (2,n+1):
            a,b=b,a+b
        return b
if __name__ =='__main__':
    s= Solution()
    print(s.fib(10))

