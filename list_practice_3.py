nums = [10,20,30,40,50]
# print(nums.reverse())
nums_sliced_rev = nums[::-1]
print(nums_sliced_rev)
nums1 = [10,20,30,40,50]
print(nums1.reverse())
nums2 = [10,20,30,40,50]
nums3 = []
for i in nums2:
    nums3.append(nums2[len(nums2)-(i+1)])
print(nums3)