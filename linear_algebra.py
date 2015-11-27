#/usr/bin/env/python
# coding: utf-8
"""this is setted for learning"""

import os
import sys
import random
import copy

print dir()
def trans(matix):
	"矩阵的转置"
	temp = copy.deepcopy(matix)
	for i in range(0, len(matix)):
		for k in range(0, len(matix)):
			for j in range(0, len(matix[i])):
				matix[i][j] = temp[j][i]

	# for m in range(len(matix) - 1, -1, -1):
	# 	for n in range(len(matix[m]) - 1, -1, -1):
	# 		matix[m][n] = temp[n][m]
	
	return matix

def printli(matix):
	"打印一个矩阵"
	for i in range(0, len(matix)):
		print "|",
		for j in range(0 , len(matix[i])):
			print matix[i][j],
		print "|"

#构造一个包含0-9的10阶矩阵"""
def builtMatix(num):
	"""#构造一个包含0-9的10阶矩阵"""
	matix = []
	num = int(num)
	for i in range(0, num):
		matix.append([])
		for j in range(0, num):
			matix[i].append(random.randint(0, 9))
	return matix


print "input a number N, and I will built a rank N matix for you with number of 0-9:"
n = raw_input(">>")
t = builtMatix(n)
printli(t)
print 
printli(trans(t))

