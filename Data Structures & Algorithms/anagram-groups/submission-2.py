class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            sorted_word = "".join(sorted(s))
            anagrams[sorted_word].append(s)
        return list(anagrams.values())