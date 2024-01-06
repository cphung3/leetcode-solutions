class Solution:
    def plusOne(self, digits):
        carryover = False
        idx = len(digits) - 1

        for i in digits[::-1]:
            print(idx, i, carryover)
            if idx == len(digits) - 1:
                if i == 9:
                    carryover = True
                    digits[idx] = 0
                else:
                    digits[idx] += 1
            else:
                if i == 9 and carryover:
                    digits[idx] = 0
                    carryover = True
                elif carryover:
                    digits[idx] += 1
                    carryover = False
                else:
                    carryover = False
            idx -= 1
        if carryover:
            return [1] + digits
        return digits
    
a = [1,2,4,9]
b = [1]
c = [9,9,9,9]

# e = 11, [1,2,3,4,5]

tests = [a, b, c]

for i in tests:
    ans = Solution().plusOne(i)
    print(ans)  
    print()
