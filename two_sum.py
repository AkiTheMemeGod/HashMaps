from collections import defaultdict
def two_sum():
    nums = [2, 4, 7, 11, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
    target = 155
    x = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in x:
            return [x[diff], i]
        x[n] = i
    return
print(two_sum())