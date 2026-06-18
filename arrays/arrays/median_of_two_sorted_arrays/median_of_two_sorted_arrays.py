class Solution:
    def medianOf2(self, a, b):
        c_array=a+b
        c_array.sort()
        num=len(c_array)
        n=num//2
        if num%2==0:
            median=(c_array[n-1]+c_array[n])/2
        else:
            median=c_array[n]      
        return median
