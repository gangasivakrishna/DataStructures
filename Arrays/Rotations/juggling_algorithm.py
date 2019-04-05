"""
array is 1 2 3 4 5 6 7
assume these array is divided into sets with d length
{1,2}{3,4}{5,6}{7}
now we are storing first element in temp variable
and assigning j+d value to jth position means at ith index
we will do this until k value is become zero

ex : arr = [1,2,3,4,5,6,7] n = 7 d =2
k = i (i=0)
1,2,3,4,5,6,7 
k = j + d (0+2)
3,2,3,4,5,6,7
k = j + d (2 +2)
3,2,5,4,5,6,7
k = j + d (4+2)
3,2,5,4,7,6,7
k = j + d (6+2)
now k>=n so k = k-n means 8-7 = 1
3,2,5,4,7,6,2
k = j + d (1 + 2)
3,4,5,4,7,6,2
k = j + d (3 + 2)
3,4,5,6,7,6,2
k = j + d (5 +2)
k>=n  k = k-n (7-7) = 0
it come out from the infinite loop
and then assign temp value to arr[j] 
now j value is 5 ..so it assigns temp value to 5th index
finally the rotated array is 3,4,5,6,7,1,2
"""

def rotateArray(arr, d, n):
    for i in range(gcd(d,n)):
        temp = arr[i]  #temp is now 1
        j = i 
        while 1 :
            k = j + d
            if(k >= n):
                k = k-n
            if (k == 0):
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp


def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a % b)
def printArray(arr, n):
    for i in range(n):
        print("%d"%arr[i],end=' ')
    print()

arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
d = 2
rotateArray(arr, d, n)
printArray(arr,n)