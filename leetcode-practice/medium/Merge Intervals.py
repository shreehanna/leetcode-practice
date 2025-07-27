class Solution:
    def merge_intervals(self, intervals):
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        merged=[intervals[0]]
        for i in intervals[1:]:
            last=merged[-1]
            if i[0]<=last[1]:
                last[1]=max(last[1], i[1])
            else:
                merged.append(i)
        return merged
if __name__ == '__main__':
    s = Solution()
    print(s.merge_intervals([[1,2],[3,4],[5,6],[7,8]]))