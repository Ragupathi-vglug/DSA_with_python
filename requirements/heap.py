import heapq
a=[]
heapq.heappush(a,5)
heapq.heappush(a,2)
heapq.heappush(a,9)
heapq.heappush(a,110)
print(a)

# Remove smallest
small=heapq.heappop(a)
print(small)

# Heapify
b=[10,5,2,62,7,3]
print(b)
heapq.heapify(b)
print(b)

# Largest element
arr=[10,5,20,15]
print(heapq.nlargest(2,arr))

# Smallest
print(heapq.nsmallest(2,arr))

# max heap
n=[]
heapq.heappush(n,-10)
heapq.heappush(n,-5)
heapq.heappush(n,-20)
heapq.heappush(n,-100)
print(heapq.heappop(n))