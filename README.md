# Solutions to LeetCode Problems

### Versions
Language | Version
------------ | -------------
C++ | C++14
Python | Python3
JavaScipt | Node.js v15.3.0

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

## Median of Two Sorted Arrays
* **[Python](https://github.com/Andrade-Diego/leetCodeSolns/blob/master/FindMediansSortedArrays.py)**
Used a pointer for each list, the smaller value goes into the new "merge" list. In order to achieve **O(log(n+m))** time, the entirety of each list is not used, only the first half + 1 of the total number of values needs to be used.
  * Runtime: 88 ms, faster than 79.72% of Python submissions.
  * Memory Usage: 14.4 MB, less than 62.34% of Python submissions.

## Distribute Candies to People
* **[Python](https://github.com/Andrade-Diego/leetCodeSolns/blob/master/distributeCandies.py)**
Used numpy for a mathy solution. Using the property that the sum of all natural numbers up to n is equal to \\[n(n+1)/2\\], to help find the answer.
  * Runtime: 91 ms, faster than 5.42% of Python submissions.
  * Memory Usage: 31.6 MB, less than 13.86% of Python submissions.

## Valid Parentheses
* **[Python](https://github.com/Andrade-Diego/leetCodeSolns/blob/master/validParentheses.py)**
Use a stack to keep track of the most recently opened parentheses type, when the program comes across a close parentheses of the right type, it pops it off the stack. If the stack is empty at the end of the string, it is a valid string.
  * Runtime: 28 ms, faster than 82.64% of Python submissions.
  * Memory Usage: 14.1 MB, less than 94.19% of Python submissions.

## Remove Duplicates From Sorted Array
* **[Python](https://github.com/Andrade-Diego/leetCodeSolns/blob/master/removeDuplicates.py)**
A fast pointer and a slow pointer are used to iterate through the list, the slow pointer stops at the first instance of each number, the fast pointer traces through the whole array and removes the element at its index if it is the same as the element at the slow pointer
  * Runtime: 96 ms, faster than 31.36% of Python submissions.
  * Memory Usage: 15.8 MB, less than 71.87% of Python submissions.

## Validate Binary Search Tree
* **[Python](https://github.com/Andrade-Diego/leetCodeSolns/blob/master/validateBST.py)**
Use DFS and recursion to iterate through tree, keep track of the lowerLimit and upperLimit for what a node value can contain.
  * Runtime: 36 ms, faster than 96.93% of Python submissions.
  * Memory Usage: 16.3 MB, less than 85.93% of Python submissions.

## Search a 2D Matrix II
* **[JavaScript](https://github.com/Andrade-Diego/leetCodeSolns/blob/master/searchMatrix.js)**
Use binary search to check each row for the target. Runtime then is O(m*logn)
  * Runtime: 2920 ms, faster than 13.9% of Python submissions.
  * Memory Usage: 41.9 MB, less than 50.8% of Python submissions.

## Transpose Matrix
* **[Python](https://github.com/Andrade-Diego/leetCodeSolns/blob/master/TransposeMatrix.py)**
Used a list comprehension for a quick, one-line solution.
  * Runtime: 60 ms, faster than 98.88% of Python submissions.
  * Memory Usage: 14.8 MB, less than 73.25% of Python submissions.

## Binary Tree Level Order Traversal
* **[Python](https://github.com/Andrade-Diego/leetCodeSolns/blob/master/BTLevelOrderTraversal.py)**
Recursive solution for level order tree traversal.
  * Runtime: 24 ms, faster than 98.92% of Python submissions.
  * Memory Usage: 15.3 MB, less than 6.84% of Python submissions.

## Single Number
* **[Python](https://github.com/Andrade-Diego/leetCodeSolns/blob/master/singleNumber.py)**

  * Runtime: 132 ms, faster than 65.57% of Python submissions.
  * Memory Usage: 16.5 MB, less than 81.41% of Python submissions.

## Remove Element
* **[Python](https://github.com/Andrade-Diego/leetCodeSolns/blob/master/RemoveElement.py)**

  * Runtime: 24 ms, faster than 98.44% of Python submissions.
  * Memory Usage: 14 MB, less than 98.6% of Python submissions.

## Merge Two Sorted Lists
* **[Python](https://github.com/Andrade-Diego/leetCodeSolns/blob/master/MergeTwoSortedLists.py)**

  * Runtime: 32 ms, faster than 91.62% of Python submissions.
  * Memory Usage: 14.1 MB, less than 95.46% of Python submissions.

## Length of Last Word
* **[Python](https://github.com/Andrade-Diego/leetCodeSolns/blob/master/LengthOfLastWord.py)**
Solution from scratch, not using rstrip() or split().
  * Runtime: 30 ms, faster than 81.62% of Python submissions.
  * Memory Usage: 14.2 MB, less than 66.42% of Python submissions.

## Plus One
* **[Python](https://github.com/Andrade-Diego/leetCodeSolns/blob/master/PlusOne.py)**

  * Runtime: 28 ms, faster than 88.89% of Python submissions.
  * Memory Usage: 14.2 MB, less than 75.49% of Python submissions.

## Two Sum ii  - Input array is sorted
* **[Python](https://github.com/Andrade-Diego/leetCodeSolns/blob/master/TwoSumII.py)**

  * Runtime: 56 ms, faster than 95.62% of Python submissions.
  * Memory Usage: 14.7 MB, less than 32.18% of Python submissions.
