import sympy
sum=0
for i in range(2000001):
    if(sympy.isprime(i)):
        sum=sum+i;
print(sum)