class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) ==0 :
            return ""

        prefix = strs[0]
        for s in range(1,len(strs)):
            while strs[s].find(prefix) != 0:
                prefix = prefix[0:len(prefix)-1]
                if prefix == "":
                    return ""
        return prefix
