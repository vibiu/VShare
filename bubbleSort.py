def bubbleSortUp(li):
	n = len(li)
	for i in range(n):
		for j in range(1, n - i):
			if li[j - 1] > li[j]:
				li[j - 1], li[j], = li[j], li[j - 1]
	return li
def bubbleSortDown(li):
	n = len(li)
	for i in range(n):
		for j in range(1, n - i):
			if li[j -1] < li[j]:
				li[j - 1], li[j] = li[j], li[j - 1]
	return li

def selectSortDown(ary):
	n = len(ary)
	for i in range(n):
		for j in range(i + 1, n):
			if ary[j] > ary[i]:
				ary[i], ary[j] = ary[j], ary[i]
	return ary

def selectSortUp(li):
	n = len(li)
	for i in range(n):
		max = i
		for j in range(i + 1, n):
			if li[j] < li[max]:
				max = j
		li[max], li[i] = li[i], li[max]
	return li



t = [3, 1, 4, 1, 5, 9]
print t
t = bubbleSortUp(t)
print t
t = bubbleSortDown(t)
print t
t = selectSortUp(t)
print t
t = selectSortDown(t)
print t