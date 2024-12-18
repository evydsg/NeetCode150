from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        if len(strs) == 0 or strs == [""]:
            return ""
        
        result = ""

        for word in strs:
            result += str(len(word)) +  "!" + word  # Fixed: str(len(word))
        
        return result

    
    def decode(self, strs: str) -> List[str]:
        if len(strs) == 0 or strs == "":
            return [strs]
        
        result = []
        index = 0

        while index < len(strs):
            secondI = index
            
            while secondI != "!":
                secondI += 1
            
            length = int(str[index : secondI])
            word = str[secondI + 1: secondI + 1 + length]

            result.append(word)
            index = secondI + 1 + length
        
        return result


