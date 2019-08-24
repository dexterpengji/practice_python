"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 3]
nums2 = [2]

The median is (2 + 3)/2 = 2.5
"""


# time complexity: O(log(M+N))
def findMedianSortedArrays(nums1, nums2):
    nums1.extend(nums2)
    nums1.sort()
    l = len(nums1)
    if l % 2 == 1:
        med = nums1[l // 2]
    else:
        med = (nums1[l // 2 - 1] + nums1[l // 2]) / 2
    return med


nums1 = [1, 3]
nums2 = [2]
print(findMedianSortedArrays(nums1, nums2))

nums1 = [1, 2]
nums2 = [3, 4]
print(findMedianSortedArrays(nums1, nums2))
