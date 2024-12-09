# NeetCode 150

Welcome to the **Neetcode 150** repository! 🎉 This repository contains solutions for the Neetcode 150 problems, following the [Neetcode.io Roadmap](https://neetcode.io/). The solutions are implemented in Python and organized by categories for easy navigation.

## About Neetcode 150
The **Neetcode 150** is a curated list of the most important coding interview problems. The problems cover a wide range of topics including arrays, strings, linked lists, dynamic programming, graphs, and more. By following the Neetcode roadmap, you can strengthen your problem-solving skills and prepare effectively for technical interviews.

## Repository Structure
The solutions are grouped by category, as outlined in the Neetcode roadmap:

neetcode-150/ ├── Arrays & Hashing/ ├── Two Pointers/ ├── Sliding Window/ ├── Stack/ ├── Binary Search/ ├── Linked List/ ├── Trees/ ├── Tries/ ├── Backtracking/ ├── Graphs/ ├── 1D Dynamic Programming/ ├── 2D Dynamic Programming/ ├── Greedy/ ├── Intervals/ ├── Math & Geometry/

bash
Copy code

## How to Use
1. **Clone the repository**:
   ```bash
   git clone https://github.com/<your-username>/neetcode-150.git
Navigate to the category of interest:
bash
Copy code
cd neetcode-150/Arrays\ &\ Hashing/
Open the solution file to explore the implementation and explanations.
Example Problem and Solution
Each solution is written with comments to explain the logic. Here's an example format:

Problem: Two Sum
Description: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

Solution:

python
Copy code
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevHash = {}

        for index, num in enumerate(nums):
            difference = target - num
            if difference in prevHash:
                return [prevHash[difference], index]
            prevHash[num] = index

