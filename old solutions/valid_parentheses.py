

def isValid(s) -> bool:
    stack = []

    parens = {
    	'(': ')',
    	'{': '}',
    	'[': ']',
    }
    for char in s:
    	if char in parens:
    		stack.append(char)
    	else:
    		if not stack:
    			return False
    		top_stack = len(stack) - 1
    		if parens[stack[top_stack]] == char:
    			del stack[-1]
    		else:
    			return False
    if len(stack):
    	return False
    return True
    
print(isValid("(](}{(])}))]"))