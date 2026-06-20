from collections import Counter,defaultdict,deque

a=[1,2,3,1,1,2,3]
print(Counter(a))
# print(Counter.most_common(1))

d=defaultdict(int)
d["apple"]+=1
print(d)

b=deque()
b.append(1)
b.append(2)
b.appendleft(10)
print(b)