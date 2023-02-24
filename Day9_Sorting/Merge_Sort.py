

# -----M E R G E S O R T------
# most optimal sorting algorithm

def merge_sort(arr):
    if len(arr) > 1:

        mid = len(arr) // 2  #--> Floor division

        Left_arr = arr [: mid]
        Right_arr = arr[mid : ]

        # Recursion 
        merge_sort(Left_arr)    
        merge_sort(Right_arr)


        i = j = k = 0
        #Copy  data to temporary array arr[k] from the Left_arry[] and Right_arr[]
        while i < len(Left_arr) and j < len(Right_arr):
            if Left_arr[i] <= Right_arr[j]:
                arr[k] = Left_arr[i]
                i += 1
            else:
                arr[k] = Right_arr[j]
                j += 1

            k += 1


        # Checking if any element was left in both arrays
        while i < len(Left_arr):
            arr[k] = Left_arr[i]
            i += 1
            k += 1

        while j < len(Right_arr):
            arr[k] = Right_arr[j]
            j += 1
            k += 1

    return arr


n = int(input("Enter Size of array : "))
arr = []
for i in range(n):
    element=int(input(f"Enter the {i} element"))
    arr.append(element)

print("Unsorted array : ",arr)

print("Sorted Array : ", merge_sort(arr))
