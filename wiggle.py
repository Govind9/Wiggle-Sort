Len = 10
combo = []
s = '0123456789'

def permute(x):
	if len(x) == Len:
		p = ''
		for i in x:
			n = int(i)
			p = p + s[n]
		combo.append(p)
	for i in range(Len):
		if s[i] not in x:
			permute(x + s[i])

def wiggle(arr):
	if len(arr) < 2:
		return arr
	l, r = 0, len(arr) - 1
	m, M = 9, 7 #Just to make sure that loop begins initially
	while True:
		l, r = 0, len(arr) - 1
		pos_m, pos_M = r, l
		m = arr[r]
		M = arr[l]
		if arr[l] > arr[r]:
			m = arr[l]
			M = arr[r]
			pos_m, pos_M = l, r
		while l < r:
			if arr[l] > arr[r]:
				temp = arr[l]
				arr[l] = arr[r]
				arr[r] = temp
			if arr[l] > M:
				M = arr[l]
				pos_M = l
			if arr[r] < m:
				m = arr[r]
				pos_m = r
			l = l + 1
			r = r - 1
		if M < m:
			break
		temp = arr[pos_m]
		arr[pos_m] = arr[pos_M]
		arr[pos_M] = temp
	mid = len(arr) / 2
	if len(arr) % 2 != 0:
		if arr[mid] < M:
			mid = mid + 1
			
	arr = wiggle(arr[:mid]) + wiggle(arr[mid:])
	return arr


#print wiggle([0, 1, 4, 2, 3, 6, 5, 9, 7, 8])

#exit()
permute('')
c = 0
for arr in combo:
	c = c + 1
	arr = list(arr)
	for i in range(len(arr)):
		arr[i] = int(arr[i])
	if wiggle(arr) != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
		print arr
