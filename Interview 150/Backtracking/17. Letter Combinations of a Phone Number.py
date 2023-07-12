class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        combos = ['']

        numMap = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
        }
        for i in digits:
            letters = numMap[int(i)]
            tempCombos = []
            temp = combos.copy()
            for j in temp:
                for k in letters:
                    res = j + k
                    tempCombos.append(res)
            combos = tempCombos
        if len(combos) == 1:
            return []
        return combos

a = '34'
b = '3456345'
c = '345734'
d = '76575'
e = ''

tests = [a,b,c,d,e]

for i in tests:
    a = Solution().letterCombinations(i)
    print(a)  
    print()