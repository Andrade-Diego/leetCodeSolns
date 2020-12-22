# Solutions to LeetCode Problems
### Versions
Language | Version
------------ | -------------
C++ | C++14
Python | Python3
## twoSum
Iterate through each element in list. Use a hash table to store difference between the current number and the target and map it to the current index. If an observed value is in the hash table, use the index of that observed value and the index it's mapped to in the table to generate the result.
* **[C++](https://github.com/Andrade-Diego/leetCodeSolns/blob/master/twoSum.cpp)**
  * Runtime: 4 ms, faster than 99.85% of C++ submissions.
  * Memory Usage: 9.4 MB, less than 76.56% of C++ submissions.
* **[Python](https://github.com/Andrade-Diego/leetCodeSolns/blob/master/twoSum.py)**
  * Runtime: 48 ms, faster than 72.41% of Python submissions.
  * Memory Usage: 14.5 MB, less than 75.5% of Python submissions.

## Container With Most Water
Use a pointer to the left of the list and the right of the list. Use the smaller of the two heights and the difference in the left and right pointer's indices to calculate the area. Keep value for area if it's larger than the previous largest. Iterate the pointer that has a smaller height at each step; reducing the width with the same height will exclusively produce smaller areas, so we don't want to keep that height for future consideration.
* **[C++](https://github.com/Andrade-Diego/leetCodeSolns/blob/master/containerWithMostWater.cpp)**
  * Runtime: 32 ms, faster than 94.11% of C++ submissions.
  * Memory Usage: 18 MB, less than 93.7% of C++ submissions.
* **[Python](https://github.com/Andrade-Diego/leetCodeSolns/blob/master/containerWithMostWater.py)**
  * Runtime: 156 ms, faster than 91.07% of Python submissions.
  * Memory Usage: 16.5 MB, less than 36.33% of Python submissions.

## Minimum Number of Steps to Make Two Strings Anagram
* **[Python](https://github.com/Andrade-Diego/leetCodeSolns/blob/master/minStepsToMakeAnagram.py)**
Used Counter() from the Collections library to count instances of characters in the string. Then iterating through the Counter object containing the two strings' difference allowed me to find the steps needed to make the second string an anagram.
  * Runtime: 252 ms, faster than 41.93% of Python submissions.
  * Memory Usage: 14.8 MB, less than 72.24% of Python submissions.

## Delete Nodes and Return Forest
* **[Python](https://github.com/Andrade-Diego/leetCodeSolns/blob/master/DelNodesGetForest.py)**
Recursive solution using preorder tree traversal
  * Runtime: 60 ms, faster than 94.37% of Python submissions.
  * Memory Usage: 15 MB, less than 14.74% of Python submissions.

