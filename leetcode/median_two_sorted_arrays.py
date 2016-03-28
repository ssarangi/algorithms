# import math
#
# cclass Solution(object):
#     def median(self, arr):
#         if len(arr) == 0:
#             return 0
#
#         if len(arr) == 1:
#             return arr[0]
#
#         if len(arr) % 2 == 1:
#             return arr[len(arr) // 2]
#         else:
#             idx = int(math.floor((len(arr) - 1) / 2))
#             n1 = arr[idx]
#             n2 = arr[idx+1]
#             return (n1 + n2) / 2.0
#
#     def findMedianSortedArrays(self, arr1, arr2):
#         if len(arr1) == 0 and len(arr2) == 0:
#             return None
#
#         if len(arr1) == 1 and len(arr2) == 1:
#             med = (arr1[0] + arr2[0]) / 2.0
#             return med
#         elif len(arr1) == 0:
#             return self.median(arr2)
#         elif len(arr2) == 0:
#             return self.median(arr1)
#
#         m1 = self.median(arr1)
#         m2 = self.median(arr2)
#
#         if m1 == m2:
#             return m1
#
#         midpt1 = (len(arr1) - 1) // 2
#         midpt2 = (len(arr2) - 1) // 2
#
#         if m1 > m2:
#             return self.findMedianSortedArrays(arr1[:midpt1+1], arr2[midpt2 + 1:])
#         else:
#             return self.findMedianSortedArrays(arr1[midpt1 + 1:], arr2[:midpt2+1])

class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        if (len(A) + len(B)) % 2 == 0:
            return (self.fms(A, B, (len(A) + len(B))/2) + self.fms(A, B, (len(A) + len(B))/2 + 1))/2.0
        else:
            return self.fms(A, B, (len(A) + len(B))/2 + 1)

    def fms(self, A, B, k):
        k = int(k)
        if len(A) > len(B):
            return self.fms(B, A, k)
        else:
            if len(A) == 0:
                return B[k-1]
            if k == 1:
                return min(A[0], B[0])
            pa = int(min(k/2, len(A)))
            pb = k - pa
            if A[pa-1] <= B[pb-1]:
                return self.fms(A[pa::], B, k-pa)
            else:
                return self.fms(A, B[pb::], k-pb)


# a1 = [1,3,5,7,9,11]
# a2 = [2,4,6,8,10,12]

a1 = [1,2,3,4,5]
a2 = [6,7,8,9,10,11]
soln = Solution()
print(soln.findMedianSortedArrays(a1, a2))
