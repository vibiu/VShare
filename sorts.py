#!uer/bin/python
#coding: utf-8
import random

def randomli(num):
	lis = []
	for i in range(0, num):
		lis.append(random.randint(1, num))
	return lis

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

def selectSortDown(li):
	n = len(li)
	for i in range(n):
		for j in range(i + 1, n):
			if li[j] > li[i]:
				li[i], li[j] = li[j], li[i]
	return li
def selectSortUp(li):
	n = len(li)
	for i in range(n):
		max = i
		for j in range(i + 1, n):
			if li[j] < li[max]:
				max = j
		li[max], li[i] = li[i], li[max]
	return li

def insertSortUp(ary):
	for i in range(1, len(ary)):
		if ary[i] < ary[i - 1]:
			temp = ary[i]
			index = i
			for j in range(i - 1, - 1, -1):
				if ary[j] >temp:
					ary[j + 1] = ary[j]
					index = j
				else: break
			ary[index] = temp
	return ary
def insertSortDown(ary):
	for i in range(1, len(ary)):
		if ary[i] > ary[i - 1]:
			temp = ary[i]
			index = i
			for j in range(i-1, -1, -1):
				if ary[j] < temp:
					ary[j + 1] = ary[j]
					index = j
				else: break
			ary[index] = temp
	return ary

t = randomli(10)
print t, "\n"

t = bubbleSortUp(t)
print t
t = bubbleSortDown(t)
print t, "\n"

t = selectSortUp(t)
print t
t = selectSortDown(t)
print t, "\n"

t = insertSortUp(t)
print t
t = insertSortDown(t)
print t, "\n"