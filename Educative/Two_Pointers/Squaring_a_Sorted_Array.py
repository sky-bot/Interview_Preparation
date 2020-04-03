def make_squares(arr):
    squares = []
    first_pointer = 0
    second_pointer = len(arr)-1

    for i in range(len(arr)):
        if arr[i] > -1:
            second_pointer = i
            break
    first_pointer = second_pointer-1

    while(len(squares)!=len(arr)):
        first = arr[first_pointer]*arr[first_pointer]
        second = arr[second_pointer]*arr[second_pointer]

        if first < second:
            squares.append(first)
            first_pointer= first_pointer-1
        else:
            squares.append(second)
            second_pointer = second_pointer + 1
               
    return squares

arr = [-2, -1, 0, 2, 3]
print(make_squares(arr))