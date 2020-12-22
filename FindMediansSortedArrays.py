def findMedianSortedArrays(nums1, nums2):
    l1 = len(nums1)
    l2 = len(nums2)
    mergeList = []
    ptr1 = 0
    ptr2 = 0
    i = 0
    while not i == ((l1 + l2) // 2 + 1):
        if (ptr1 < l1 and ptr2 < l2):
            if nums1[ptr1] > nums2[ptr2]:
                mergeList.append(nums2[ptr2])
                ptr2 += 1
            else:
                mergeList.append(nums1[ptr1])
                ptr1 += 1
        elif (ptr1 >= l1):
                mergeList.append(nums2[ptr2])
                ptr2 += 1
        elif (ptr2 >= l2):
                mergeList.append(nums1[ptr1])
                ptr1 += 1
        i += 1
    soln = 0
    if (l1 + l2) % 2 == 0:
        soln = (mergeList[-1] + mergeList[-2]) / 2
    else: soln = mergeList[-1]
    return soln

if __name__ == "__main__":
    nums1 = [2, 7, 11, 15]
    nums2 = [3, 9, 37]
    print(f"(TEST 1)\n\tList 1: {nums1}\n\tList 2: {nums2}\n\tResult: {findMedianSortedArrays(nums1, nums2)}")
    nums1 = [1, 2, 3, 4]
    nums2 = [5, 6]
    print(f"(TEST 2)\n\tList 1: {nums1}\n\tList 2: {nums2}\n\tResult: {findMedianSortedArrays(nums1, nums2)}")