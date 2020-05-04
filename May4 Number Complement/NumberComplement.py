class Solution:
    def findComplement(self, num: int) -> int:
        num = (bin(num))
        res = ''.join(['0' if r == '1' else '1' for r in num[2:]])
        return int(res,2)

        
