class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        hashS = {}       
        for i in S:
            if i not in hashS:
                hashS[i] = 1
            else:
                hashS[i]+=1
            
        count = 0
        
        for i in J:
            if i in hashS:
                count+=hashS[i]
        return count
        
