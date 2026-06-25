class Solution:
    def getSum(self, a: int, b: int) -> int:
    #    return int(math.log(math.exp(a)* math.exp(b)))
        mask = 0xffffffff
        while (mask&b) > 0:
            a,b = a^b, (a&b)<<1
            print(bin(a), bin(b), bin(mask&b))
        return (mask&a) if b > 0 else a