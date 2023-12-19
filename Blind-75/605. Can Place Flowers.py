class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        total = n
        counter = 0
        newbed = [0] + flowerbed + [0]

        for n in newbed:
            if n == 1:
                added_flowers = (counter - 1)//2
                total -= added_flowers
                counter = 0
            elif n == 0:
                counter += 1
            
            # print(n, total, counter)
            if total <= 0:
                return True
        added_flowers = (counter - 1)//2
        total -= added_flowers
        return total <= 0
    

a = [1,0,0,0,0,1], 2
b = [1,0,0,0,1,0,0], 2

# e = 11, [1,2,3,4,5]

tests = [a, b]

for i, j in tests:
    ans = Solution().canPlaceFlowers(i, j)
    print(ans)  
    print()

# 140ms
# Beats 93.01%of users with Python3 