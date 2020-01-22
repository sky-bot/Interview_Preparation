def cal_fibonacci(nth):
    fibo = [0, 1]
    for i in range(2, nth+1):
        fibo.append(fibo[i-2]+fibo[i-1])
    
    progress(fibo)
    return fibo[-1]

def progress(fibo):
    print(fibo)

target = 5
print(cal_fibonacci(target))