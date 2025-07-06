class Solution:
    def twoSum(self, nums, target):
        seen={}
        for i , j in enumerate(nums):
            word=target - j
            if word in seen:
                return [seen[word], i]
            seen[j] = i
if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    s = Solution()
    print(s.twoSum(nums, target))
