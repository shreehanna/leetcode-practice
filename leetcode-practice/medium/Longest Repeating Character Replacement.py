from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s,k):
        count=defaultdict(int)
        max_freq=0
        left=0
        max_length=0
        for i in range(len(s)):
            count[s[i]] +=1
            max_freq=max(max_freq, count[s[i]])
            if (i-left+1)-max_freq>k:
                count[s[i]] -=1
                left+=1
            max_length=max(max_length,i-left+1)
        return max_length
if __name__ == '__main__':
    s=Solution()
    print(s.lengthOfLongestSubstring("abcabcbb",2))


