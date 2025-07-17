class solution(object):
    def reverseString(self, s: list[str]) -> None:
        l=0
        r=len(s)-1
        while l<r:
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1
if __name__ == '__main__':
    input_list = ['h', 'e', 'l', 'l', 'o']
    s = solution()
    s.reverseString(input_list)
    print(input_list)