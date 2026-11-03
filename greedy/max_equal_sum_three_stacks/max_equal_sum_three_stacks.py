class Solution:
    def maxEqualSum(self, s1, s2, s3):
        sum1 = sum(s1)
        sum2 = sum(s2)
        sum3 = sum(s3)

        i = j = k = 0

        while i < len(s1) and j < len(s2) and k < len(s3):
            if sum1 == sum2 == sum3:
                return sum1

            if sum1 >= sum2 and sum1 >= sum3:
                sum1 -= s1[i]
                i += 1

            elif sum2 >= sum1 and sum2 >= sum3:
                sum2 -= s2[j]
                j += 1

            else:
                sum3 -= s3[k]
                k += 1

        return 0
