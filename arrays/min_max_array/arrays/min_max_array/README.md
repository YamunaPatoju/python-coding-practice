Minimum and Maximum of an Array
Problem Statement

Given an array of integers, find the minimum and maximum elements present in the array.

Example

Input:

[3, 5, 1, 8, 2]

Output:

Minimum = 1

Maximum = 8

Approach
Assume the first element is both minimum and maximum.
Traverse the array.
If an element is smaller than the current minimum, update minimum.
If an element is larger than the current maximum, update maximum.
Return both values.
