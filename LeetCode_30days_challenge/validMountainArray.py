class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if len(arr) <=2:
            return False
        
        upside =  False
        downside = False
        
        if arr[0] < arr[1]:
            upside  = True
        
        for i in range(len(arr)-1):
            print(arr[i])
            if arr[i] < arr[i+1] and upside and not downside:
                continue
            else:
                if arr[i] > arr[i+1]:
                    print(arr[i], arr[i+1])
                    downside = True
                else:
                    return False
                
        
        return True if downside==True and upside ==True else False
        
