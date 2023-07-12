class MinStack:

    def __init__(self):
        self.minStack = []
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.minStack) and self.minStack[-1] >= val:
            self.minStack.append(val)
        elif not len(self.minStack):
            self.minStack.append(val)

        self.stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if self.minStack[-1] == val:
            self.minStack.pop() 

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

a = ["MinStack","push","push","push","getMin","pop","top","getMin"]
# b = '/../'
# c = "/home//foo/"
# d = "/../..././/./"
# e = "/...../.kdf//..d./"

tests = [a]


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
a = minStack.getMin() # return -3
minStack.pop()
b = minStack.top()    # return 0
c = minStack.getMin() # return -2

for i in [a,b,c]:
    print(i)