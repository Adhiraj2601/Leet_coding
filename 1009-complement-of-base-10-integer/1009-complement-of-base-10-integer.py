class Solution:
    def bitwiseComplement(self, n: int) -> int:
        b = bin(n)[2:]
        temp = '1'*len(b)
        comp = int(temp) - int(b)
        return int(str(comp), 2)
        