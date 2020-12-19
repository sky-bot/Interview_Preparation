class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    
        can_placed = 0
        
        if len(flowerbed)==1:
            if 1 in flowerbed:
                can_placed = 0
            else:
                can_placed = 1
        else:
            i=0
            while(i<len(flowerbed)-1):
                print("index: ",i)
                if flowerbed[i]==0 and flowerbed[i+1]==0:
                    flowerbed[i] = 1
                    can_placed += 1
                    i+=2
                elif flowerbed[i]==1:
                    i+=2
                else:
                    i+=1
        
            if flowerbed[-1]==0 and flowerbed[-2]==0:
                can_placed +=1
                flowerbed[-1]=1
        print(can_placed, flowerbed)
        if n <= can_placed:
            return True
        
        return False
