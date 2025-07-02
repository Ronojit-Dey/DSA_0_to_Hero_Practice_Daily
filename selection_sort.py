def selection_sort(nums):
    n = len(nums)

    for i in range(0, n-1):
        mini = i
        for j in range(i+1,n):
            if nums[j] < nums[mini]:
                mini = j
        temp = nums[mini]
        nums[mini] = nums[i]
        nums[i] = temp

    return nums

print(selection_sort([21,33,12,44,21,11,3]))












