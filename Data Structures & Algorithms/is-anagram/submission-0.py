class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        for ch in s:
            if ch in letters:
                letters[ch] += 1
                continue
            letters[ch] = 1
        
        for ch in t:
            if ch in letters:
                letters[ch] -= 1
                if letters[ch] == 0:
                    del letters[ch]
            else:
                return False
        
        if not letters:
            return True
        return False