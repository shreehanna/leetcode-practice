class solution:
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
if __name__ == '__main__':
    s = solution()
    print(s.containsDuplicate([1, 1, 2]))
    print(s.containsDuplicate([1, 1, 2, 2]))
