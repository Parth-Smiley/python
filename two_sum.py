ls = [2,3,4,5,8]
target = 13
low = 0
high = len(ls)-1
def two_sum(ls,target):
    if ls[low]+ls[high] == target:
        return low,high
    else:
        two_sum(ls[low+1:high])

print(two_sum(ls,target))