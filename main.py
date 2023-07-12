def arrar_rotation(array, a, b):

    while(a < b):
        array[a], array[b] = array[b], array[a]
        a += 1
        b -= 1

array = list(map(int, input().split()))
k = int(input())
if k >= len(array):
    k = len(array) % k
length = len(array)-1

arrar_rotation(array, 0, length)
arrar_rotation(array, 0, k-1)
arrar_rotation(array, k, length)

print(array)


