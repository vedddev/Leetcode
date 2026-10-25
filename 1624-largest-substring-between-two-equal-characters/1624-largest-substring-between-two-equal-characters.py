class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        mp = {}
        max_len = -1

        for i, ch in enumerate(s):
            if ch in mp:
                max_len = max(max_len, i - mp[ch] - 1)
            else:
                mp[ch] = i

        return max_len