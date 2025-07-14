class Solution:
    def findMaxAverage(self, nums,k) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)
        return max_sum / k
if __name__ == '__main__':
    s = Solution()
    print(s.findMaxAverage([1,2,3,4,5], 4))