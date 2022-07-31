def merge_nums_arrays(n1, n2):
    i1 = 0
    i2 = 0
    res = []
    while i1 < len(n1) and i2 < len(n2):
        if n1[i1] < n2[i2]:
            res.append(n1[i1])
            i1+=1
        else:
            res.append(n2[i2])
            i2+=1
    if i1 < len(n1):
        res += n1[i1:]
    if i2 < len(n2):
        res += n2[i2:]
    return res

if __name__ == "__main__":
    nums1 = [1,3,4,7,8,11, 18, 19, 20]
    nums2 = [2,3,5,9,16]
    print(merge_nums_arrays(nums1, nums2))
