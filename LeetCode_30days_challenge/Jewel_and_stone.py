def numJewelsInStones(J, S):
        stone = dict()
        for ch in S:
            stone[ch] = stone.get(ch) + 1 if stone.get(ch) else 1
        
        result = 0
        for ch in J:
            result = result + stone.get(ch) if stone.get(ch) else result
        
        return result

J = 'ebd'
S= 'bbb'