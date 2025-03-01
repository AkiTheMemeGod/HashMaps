from collections import defaultdict
def two_sum():

    x = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in x:
            return [x[diff], i]
        x[n] = i
    return
print(two_sum())