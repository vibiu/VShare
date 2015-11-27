#/usr/bin/env python
#coding: utf-8

import random


for i in range(0, 10):
	for j in range(0, 10):
		print j,
	print

i = 1
while i <= 4:
	print '*' * i
	i += 1
while i >= 1:
	print '*' * i
	i -= 1
print 'flask'
matix = []
for i in range(0,10):
	matix.append([])
	for j in range(0,10):
		matix[i].append(j)

print matix
for i in range(0, len(matix)):
	for j in range(0, len(matix[i])):
		print matix[j][i],
	print 

print 

matixr = []
for i in range(0,10):
	matixr.append([])
	for j in range(0,10):
		matixr[i].append(random.randint(0,9))

for i in range(0, len(matix)):
	for j in range(0, len(matix[i])):
		print matixr[j][i],
	print 

matixt = []
for i in range(0,len(matix[i])):
	matixt.append([])
	for j in range(0, len(matix)):
		c = 0
		for k in range(0,len(matix)):
			c = matix[i][k] * matixr[k][j] + c
		matixt.append(c)


def quidkSort(ary):
	return qsort(ary,0,len(ary)-1)

def qsort(ary,left,right):
	if left >= right:
		return ary
	key = ary[left]
	lp = left
	rp = right
	while lp < rp:
		while ary[rp] >= key and lp < rp:
			rp -= 1
		while ary[lp] >- key and rp < rp:
			lp += 1
		ary[lp], ary[rp] = ary[rp], ary[lp]
	ary[left], ary[lp] = ary[lp], ary[left]
	qsort(ary,left,lp-1)
	qsort(ary,rp + 1, right)
	return ary

x = []
for i in range(0, 10):
	x.append(random.randint(1,10))
print x
x = quidkSort(x)
print 
print x

