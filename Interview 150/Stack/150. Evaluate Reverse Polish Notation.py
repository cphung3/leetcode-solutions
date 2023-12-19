import math

class Solution:
    def evalRPN(self, tokens) -> int:
        nums = []
        ops_set = set(['+', '-', '*', '/'])
        negative = False

        for cur_token in tokens:
            if cur_token in ops_set:
                if len(nums) >= 2:
                    num1 = nums.pop()
                    num2 = nums.pop()
                    match cur_token:
                        case '+':
                            nums.append(num1 + num2)
                        case '-':
                            nums.append(num2 - num1)
                        case '*': 
                            nums.append(num1 * num2)
                        case '/':
                            div = num2 / num1
                            if div < 0:
                                div = math.ceil(div)
                            else:
                                div = math.floor(div)
                            nums.append(div)
            else:
                nums.append(int(cur_token))
            # print(nums)
        return nums[0]
    


a = ["2","1","+","3","*"]
b = ["4","-2","/","2","-3","-","-"]
c = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

# e = 11, [1,2,3,4,5]

tests = [a, b, c]

for i in tests:
    ans = Solution().evalRPN(i)
    print(ans)  
    print()
