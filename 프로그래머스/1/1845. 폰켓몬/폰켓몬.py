def solution(nums):
    r = set(nums)
    print(r)
    if (len(nums)/2)<len(r):
        return len(nums)/2
    else:
        return len(r)