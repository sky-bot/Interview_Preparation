
def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
    lower = 1
    upper = n
    while(lower<=upper):
        mid = int((lower + upper) / 2)
        result = fun(mid )
        
        if not result:
            lower = mid 
        else:
            upper = mid
        
        if lower+1 == upper:
            return upper
        
    return upper

def fun(a):     
    if a <= 1:
        return False
    else:
        return True

print(firstBadVersion(3))