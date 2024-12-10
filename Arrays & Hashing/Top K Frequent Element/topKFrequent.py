import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        result = []

        for num in nums:
            if num in dictionary:
                dictionary[num] += 1
            else:
                dictionary[num] = 1
        
        max_heap = [(-value, key) for key, value in dictionary.items()]

        for index in range(k):
            value, key = heapq.heappop(max_heap)
            result.append(key)
            
        return result

