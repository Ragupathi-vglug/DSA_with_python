import bisect
arr=[1,2,4,4,5]
print(bisect.bisect_left(arr,4))

# Bisect right
print(bisect.bisect_right(arr,4))

# insort
a=[1,2,5,7]
bisect.insort(a,4)
print(a)