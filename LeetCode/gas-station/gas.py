def canCompleteCircuit(gas, cost):
    
    length = len(gas)

    for i in range(len(gas)):
        startIndex = i
        temp = 0
        gasAval = 0

        while(temp < length):
            gasAval = gas[temp] + gasAval
            costNext = cost[temp]

            if(gasAval < costNext):
                break
            else:
                gasAval = gasAval - costNext
            temp = temp + 1

        if temp == length:
            return startIndex
        else:
            firstGas = gas.pop(0)
            gas.append(firstGas)
            firstCost = cost.pop(0)
            cost.append(firstCost)
    
    return -1

gas = [2, 3, 4]
cost = [3, 4, 3]
print(canCompleteCircuit(gas, cost))
