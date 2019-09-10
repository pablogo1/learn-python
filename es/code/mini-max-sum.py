# Mini-Max Sum
def min_max_sum(arr):
    arr.sort()
    return sum(arr[:4]), sum(arr[1:4])

arr = [793810624, 895642170, 685903712, 623789054, 468592370]
min, max = 2572095760, 2999145560

print (min)
print (max)

print(min_max_sum(arr))
