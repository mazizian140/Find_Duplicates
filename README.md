﻿# Find_Duplicates

 Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is 
the smallest in lexicographical order among all possible results.

Algorithm
Greedy Choice: Keep track of the last occurrence of each character in the string to ensure that you don't remove necessary characters.
Stack Approach: Use a stack to build the result, maintaining lexicographical order. If the current character is smaller than the previous character 
(from the stack) and the previous character appears later in the string, pop the previous character to maintain lexicographical order.
Visited Set: Keep track of characters that are already in the result to ensure every character appears only once.
