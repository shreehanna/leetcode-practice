class solution:
    def numOfSteps(self, num):
        steps = 0
        while num > 0:
            if num % 2 == 0:
                num //= 2
            else:
                num-=1
                steps +=1
        return steps
if __name__=='__main__':
    s=solution()
    print(s.numOfSteps(14))