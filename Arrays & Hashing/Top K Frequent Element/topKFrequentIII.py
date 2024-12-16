def topKFrequent(self, nums: List[int], k:int) -> List[int]:
    dictionary = {}
    freq = [[] for index in range(len(nums) + 1)]
    result = []

    for num in nums:
            if num in dictionary:
                dictionary[num] += 1
            else:
                dictionary[num] = 1

    for num, frequency in dictionary.items():
        freq[frequency] = num
    
    for index in range(len(freq) - 1, 0, -1):
        for number in frequency[index]:
            result.append(number)

            if len(result) == k:
                return result
        