class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            length = str(len(word))
            encoded_str += length + "#" + word

        return encoded_str

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            j += 1
            result.append(s[j: j + length])

            i = j + length
        return result

        