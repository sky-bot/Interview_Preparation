def findComplement(num):
    binary = list(bin(num).replace('0b', ""))
    invertedBinary = list()
    for x in binary:
        if x == '0':
            invertedBinary.append('1')
        else: 
            invertedBinary.append('0')

    invertedBinaryString = "".join(invertedBinary)
    
    return int(invertedBinaryString, 2)

num = 5
print(findComplement(5))