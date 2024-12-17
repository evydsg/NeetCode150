from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        if len(strs) == 0 or strs == [""]:
            return ""
        
        result = ""

        for word in strs:
            result += "!" + str(len(word)) + word  # Fixed: str(len(word))
        
        return result

# Test
dummy_input = ["Hello", "World"]
codec = Codec()
print(codec.encode(dummy_input))  # Output: encoded string
