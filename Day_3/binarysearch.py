def binary_search(arr,target):
    left =0
    right=len(arr)-1
    
    while left <= right:
        mid = (left+right)//2
        
        if arr[mid]==target:
            return mid
        
        elif arr[mid]<target:
            left = mid +1
            
        else:
            right=mid-1
            
    return -1

numbers=[10,11,12,13,14]
target_input=input("enter the number")
target=int(target_input)
result=binary_search(numbers,target)

if result != -1:
    print(f"element found at index {result}")
else:
    print("element not found")
    