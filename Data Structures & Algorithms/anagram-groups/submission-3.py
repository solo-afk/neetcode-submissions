class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups ={}
        for word in strs:
            ltrs = [0] * 26
            for ch in word:
                ltrs[ord(ch) - ord('a')] += 1
            ltrsTuple = tuple(ltrs)
            if ltrsTuple in groups:
                groups[ltrsTuple].append(word)
            else:
                groups[ltrsTuple] = [word]
        
        return list(groups.values())
    
            
