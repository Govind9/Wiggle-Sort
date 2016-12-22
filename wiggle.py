def wiggle(arr):
	print arr
	if len(arr) == 1:
		return arr
	m, M = 7, 9
	while M > m:
		l, r = 0, len(arr) - 1
		mins = []
		maxs = []
		if arr[l] < arr[r]:
			M = arr[l]
			if arr[l + 1] > arr[r]:
				m = arr[l + 1]
			else:
				m = arr[r]
		else:
			M = arr[r]
			if arr[r - 1] > arr[l]:
				m = arr[r - 1]
			else:
				m = arr[l]
		while l <= r:
			if arr[l] < arr[r]:
				mins.append(arr[l])
				if arr[l] > M:
					M = arr[l]
				l = l + 1
			else:
				mins.append(arr[r])
				if arr[r] > M:
					M = arr[r]
				r = r - 1
			if r < l:
				break
			
			if arr[l] > arr[r]:
				maxs.append(arr[l])
				if arr[l] < m:
					m = arr[l]
				l = l + 1
			else:
				maxs.append(arr[r])
				if arr[r] < m:
					m = arr[r]
				r = r - 1
		arr = mins + maxs
	if len(arr) % 2 == 0:
		mid = len(arr) / 2
	else:
		mid = (len(arr) / 2) + 1
	arr = wiggle(arr[:mid]) + wiggle(arr[mid:])
	return arr

arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
arr = wiggle(arr)
print arr

