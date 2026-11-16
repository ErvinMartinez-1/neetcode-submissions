class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding = ""
        for s in strs:
            wordLen = len(s)
            encoding += str(wordLen) + "#" + s
        return encoding

    def decode(self, s: str) -> List[str]:
        answer = []
        l = 0
        while l < len(s):
            length = ""
            while s[l] != '#':
                length += s[l]
                l += 1
            l += 1
            length = int(length)
            word = s[l: l + length]
            answer.append(word)
            l += length

        return answer


