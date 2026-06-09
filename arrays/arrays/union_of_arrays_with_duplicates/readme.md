Union of Two Arrays with Duplicates
Problem Statement-

Given two arrays that may contain duplicate elements, find the union of the arrays.

The union contains all distinct elements present in either array.

Example-

Input:

arr1 = [1, 2, 2, 3, 4]

arr2 = [2, 3, 5, 5]

Output:

[1, 2, 3, 4, 5]

Approach-

1.Create an empty set.

2.Traverse the first array and add elements to the set.

3.Traverse the second array and add elements to the same set.

4.Convert the set into a list.

5.Return the result.

##A set automatically removes duplicate values.##
