def getMissingNumber(n,arr):
    ans = 0
    for i in range(1,n+1): ans = ans^i

    for i in range(len(arr)):
        ans = ans^arr[i]

    return ans


def main():
    n = 10
    arr = [3,9,1,10,7,4,2,5,6]
    ans = getMissingNumber(n,arr)
    print(ans)

main()