# Max Product Subset

## Problem
Given an array of integers, find the maximum product possible from a non-empty subset. Return the product modulo `10^9 + 7`, except when the maximum product is negative, as required by the expected output.

## Approach
- Multiply all non-zero elements.
- Count the negative numbers.
- If the number of negative elements is odd, exclude the negative number closest to zero to maximize the product.
- Handle single-element arrays and zeros separately.

## Algorithm
1. Initialize the product to `1`.
2. Multiply all non-zero elements and store negative numbers.
3. If the array contains only one element, return it directly.
4. If the number of negative elements is odd, divide the product by the largest negative number.
5. Handle the zero-only product case.
6. Return the result modulo `10^9 + 7`.

