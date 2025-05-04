# Python Program check if there are any duplicates   




def check_duplicates(arr):
    n = len(arr)
    
    # Outer loop to pick each element one by one
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                return True 
    return False


if __name__ == '__main__':
    nums = [int() for i in input().split()]
    print(check_duplicates(nums))



   
