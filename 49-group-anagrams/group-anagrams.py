class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = defaultdict(list)
        for s in strs:
            d["".join(sorted(s))].append(s)

        return list(d.values())