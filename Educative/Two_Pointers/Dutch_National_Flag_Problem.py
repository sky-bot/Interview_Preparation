
def dutch_flag_sort(arr):
    first = 0
    last = len(arr) - 1
    i=0
    while(i<=last):
        if arr[i] == 2:
            swap(arr, i, last)
            last -= 1
            if arr[i]==2:
                continue
        
        if arr[i] == 0:
            swap(arr, i, first)
            first += 1
        i+=1
            
    return arr

def swap(arr, first, second):
    temp = arr[first]
    arr[first] = arr[second]
    arr[second] = temp



arr = [2, 2, 0, 1, 0, 1, 2, 2, 0]
print(dutch_flag_sort(arr))