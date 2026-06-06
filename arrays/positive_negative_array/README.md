Move All Negative Elements to End

Problem Statement-

Given an array of positive and negative integers, move all negative elements to the end of the array.

Example-

Input:

[1, -2, 3, -4, 5, -6]

Output:

[1, 3, 5, -2, -4, -6]

Approach-

1.Create two separate lists:

-positive for storing positive numbers and zero.

-negative for storing negative numbers.

2.Traverse the array.

3.Add each element to the appropriate list.

4.Combine positive and negative lists.
Update the original array.
