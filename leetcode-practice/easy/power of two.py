class solution:
    def power(self,n):
        if n<=0:
            return False
        return (n&(n-1))==0
if __name__=='__main__':
    s = solution()
    print(s.power(4))
    print(s.power(7))