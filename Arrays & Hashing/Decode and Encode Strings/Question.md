# 271. Encode and Decode Strings

## Problem

Design an algorithm to encode a list of strings into a single string. The encoded string is then sent over the network and is decoded back to the original list of strings.

---

### **Machine 1 (Sender)**

The sender has the function:

```cpp
string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (Receiver)
The receiver has the function:

cpp

vector<string> decode(string s) {
  // ... your code
  return strs;
}

Workflow
Machine 1 encodes a list of strings into a single string:
string encoded_string = encode(strs);

Machine 2 decodes the encoded string back into the original list:
vector<string> strs2 = decode(encoded_string);

The output strs2 should match the original input strs.
Examples:

Example 1
Input:
dummy_input = ["Hello", "World"]

Output:
["Hello", "World"]

Explanation:

Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 sends the encoded msg to Machine 2.

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);
Example 2
Input:
dummy_input = [""]

Output:
[""]

Constraints
strs[i] contains any possible characters out of 256 valid ASCII characters.

Notes
You are not allowed to use any serialization methods such as eval.