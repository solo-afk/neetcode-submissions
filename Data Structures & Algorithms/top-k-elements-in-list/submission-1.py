class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        maxes = []
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        
    
        for i in range(k):
            max_value = max(dict.values())
            for key in dict:
                if dict[key] == max_value:
                    maxes.append(key)
                    del dict[key]
                    break
        
        return maxes