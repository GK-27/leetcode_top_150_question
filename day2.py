

def isduplicate(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                return True
    return False

if __name__ == '__main__':
    nums = [int() for i in input().split()]
    print(isduplicate(nums))


            
            

   
