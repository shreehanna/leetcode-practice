class Solution:
    def maxSubArray(self, nums) -> int:
        max_sum = nums[0]
        current_sum = nums[0]
        for i in range(1, len(nums)):
            current_sum = max(current_sum + i,i)
            max_sum = max(max_sum, current_sum)
        return max_sum
if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
