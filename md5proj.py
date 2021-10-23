str_lst = ['a','a','a','a','a','a']

for i  in range(26):
	str_lst[1] = 'a'
	for i  in range(26):
		str_lst[2] = 'a'
		for i  in range(26):
			str_lst[3] = 'a'
			for i  in range(26):
				str_lst[4] = 'a'
				for i  in range(26):
					str_lst[5] = 'a'
					for i  in range(26):
						print("".join(str_lst))
						str_lst[5] = chr(ord(str_lst[5])+1)
					str_lst[4] = chr(ord(str_lst[4])+1)
				str_lst[3] = chr(ord(str_lst[3])+1)
			str_lst[2] = chr(ord(str_lst[2])+1)
		str_lst[1] = chr(ord(str_lst[1])+1)
	str_lst[0] = chr(ord(str_lst[0])+1)
