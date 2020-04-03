# N = input()
# N = 10
# hand = list()

# for i in range(0, 10):
#     temp = input()
#     temp = temp.split(" ")
#     temp = [int(i) for i in temp]
#     hand.append(temp)
hand = [
    [7, 3, 11, 4, 5, 6, 1, 2, 8, 9], 
    [1, 11, 10, 5, 6, 8, 3, 7, 4, 2], 
    [9, 3, 2, 7, 5, 8, 10, 4, 1, 11], 
    [8, 2, 5, 10, 3, 6, 4, 7, 9, 1], 
    [3, 10, 2, 11, 7, 9, 1, 5, 6, 4], 
    [5, 11, 1, 3, 8, 10, 4, 6, 2, 9], 
    [11, 1, 8, 7, 3, 2, 10, 6, 5, 9], 
    [4, 1, 5, 11, 10, 6, 3, 2, 9, 7], 
    [2, 1, 9, 11, 8, 6, 7, 10, 3, 4], 
    [10, 5, 4, 1, 3, 6, 2, 11, 7, 8]
]

dislike = dict()
for row in hand:
    temp = row.pop(0)
    dislike[temp] = row

for i in range(1,11):
    if dislike.get('i'):
        