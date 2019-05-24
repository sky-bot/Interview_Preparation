
# a = 600851475143;
# big=2
# prime=0;
# for i in range(2,a+1):
#     for j in range(1,i+1):
#         if(i%j==0):
#             prime = prime+1
#     if(prime==2):
#         if(a%i==0):
#             big=i
#     prime=0 
# print(big)

import sympy
a = 600851475143;
big=2
for i in range(2,a+1):
    if(sympy.isprime(i) and a%i==0 ):
      big=i
print(big)