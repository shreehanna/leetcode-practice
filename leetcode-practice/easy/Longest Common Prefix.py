class solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        prefix = strs[0]
        for word in strs[1:]:
            while word[:len(prefix)] != prefix:
                prefix =prefix[:-1]
                if not prefix:
                    return ""
        return prefix
if __name__ == '__main__':
    s = solution()
    print(s.longestCommonPrefix(["flower","flow","flight"]))