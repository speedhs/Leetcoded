class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = 0
        for i in jewels:
            for j in stones:
                if i == j:
                    counter += 1
        return counter