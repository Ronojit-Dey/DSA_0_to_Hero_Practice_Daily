
def insertion_sort(nums):
    n = len(nums)

    for i in range(0,n):
        key = nums[i]
        j = i - 1

        while j > 0 and key < nums[j]:
            nums[j+1] = nums[j]
            j = j - 1
            nums[j+1] = key
    
    return nums

print(insertion_sort([1,12,30,12,2,1,15,16]))
