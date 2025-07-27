class Solution:
    def containerWithMostWater(self, height):
        left=0
        right=len(height)-1
        max_area=0
        while left < right:
            width= right - left
            new_height=max(height[left],height[right])
            area=new_height*width
            max_area=max(max_area,area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_area
if __name__ == '__main__':
    s = Solution()
    print(s.containerWithMostWater([2,3,1,1,4]))
    print(s.containerWithMostWater([2,2]))
