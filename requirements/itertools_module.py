from itertools import *

# Count()
for i in count(5):
    if i==1000:
        break
    print(i)

# cycle()
for i in cycle("ABC"):
    print(i)

# repeat()
for i in repeat("Ragu",10):
    print(i)

# permutation()
print(list(permutations([1,2,3])))

# combinational
print(list(combinations([1,2,3],2)))

# product
for i in product([1,2,3],["A","B","C"]):
    print(i)

# accumulator
print(list(accumulate([1,2,3,4,5])))
