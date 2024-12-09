class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0 or strs == [""]:
            return [strs]
        
        dictionary = {}

        for word in strs:
            key = "".join(sorted(word))

            if key in dictionary:
                dictionary[key].append(word)
            else:
                dictionary[key] = [word]
        
        return list(dictionary.values())