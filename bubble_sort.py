
def bubble_sort(nums):
    n = len(nums)
    for i in range(0,n-1):
        swapped = False

        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums

print(bubble_sort([12,3,43,2,12,13,55]))

