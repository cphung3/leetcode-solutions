

def sum_int(a, b):

	if a < 0:
		add = False
		neg_a = 3
		neg_b = 2
	if b < 0:
		add = False
		neg_b = 3
		neg_a = 2
	if a >= 0 and b >= 0:
		add = True
		neg_a = 2
		neg_b = 2


	bin_a = list(bin(a)[neg_a:][::-1])
	bin_b = list(bin(b)[neg_b:][::-1])
	max_length = max(len(bin_a), len(bin_b))



	index = 0
	if len(bin_a) > len(bin_b):
		while len(bin_a) > len(bin_b):
			bin_b.append('0')
	elif len(bin_b) > len(bin_a):
		while len(bin_b) > len(bin_a):
			bin_a.append('0')
	carry = False
	print(bin_a, bin_b)
	result = []
	for i in range(max_length):		
		idx_a = bin_a[i]
		idx_b = bin_b[i]
		if idx_a == '1' and idx_b == '1': # both ones
			print("here", idx_a, idx_b)

			if carry: result.append('1')
			else: result.append('0')
			carry = True
		elif idx_a == '1':
			if carry: 
				result.append('0')
				carry = True
			else: 
				result.append('1')
				carry = False
		elif idx_b == '1': 
			if carry: 
				result.append('0')
				carry = True
			else: 
				result.append('1')
				carry = False
		else:
			print("else", idx_a, idx_b)

			if carry: result.append('1')
			else: result.append('0')
			carry = False
	if carry and add:
		result.append('1')

	print(result)
	result.append('0b')
	result.reverse()
	answer = int(''.join(result), 2)
	return answer

a = sum_int(-2,4)
print(a)