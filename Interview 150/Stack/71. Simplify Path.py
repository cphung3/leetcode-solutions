class Solution:

    SEP = '/'
    CURRENT_DIR = '.'
    PARENT_DIR = '..'

    def simplifyPath(self, path: str) -> str:
        simplified = []
        for directory in path.split(self.SEP):
            if not directory or directory == self.CURRENT_DIR:
                continue

            if directory == self.PARENT_DIR:
                if simplified:
                    simplified.pop()
            else:
                simplified.append(directory)

        return self.SEP + self.SEP.join(simplified)
    
a = '/home/'
b = '/../'
c = "/home//foo/"
d = "/../..././/./"
e = "/...../.kdf//..d./"

tests = [a,b,c,d,e]

for i in tests:
    a = Solution().simplifyPath(i)
    print(a)  
    print()