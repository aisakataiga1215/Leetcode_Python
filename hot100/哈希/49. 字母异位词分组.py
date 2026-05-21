from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        for s in strs:
            news = "".join(sorted(s))
            hash[news].append(s)
        return list(hash.values())
