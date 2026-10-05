class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = {} #mapping count to list of anagrams

        for s in strs:
            count = [0] * 26 # a through z characters

            for c in s:
                count[ord(c) - ord("a")] += 1

            key = tuple(count)
            if key not in res:
                res[key] = []
            res[key].append(s)

        return list(res.values())

        