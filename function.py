#!/usr/bin/python
# -*- coding: UTF-8 -*-


# def fib(n):
# 	'''get a list of fibnacci series to n'''
# 	a, b = 0, 1
# 	result = []
# 	while a<n:
# 	result.append(a)
# 	a, b = b, a+b
# 	return result

def factorial(x):
	"""define factorial"""
	j = 1
	k = range(1, x + 1)
	for m in k:
		i = m
		j = j * i
	return(j)


def arrangement(x, y):
	"""define arrangement"""
	t = factorial(x) / factorial(x - y)
	return(t)


def combination(x,y):
	"""define combination"""
	f = arrangement(x,y) / arrangement(y,y)
	return(f)


def caps(x):
	'''define turn lowercase to capitalization'''
	t = '' 
	for i in x:
		m = chr(ord(i) - 32)
		t = t + m
	return(t)


def lowe(x):
	'''define turn capitalization to lowercase'''
	t = ''
	for i in x:
		m = chr(ord(i) + 32)
		t = t + m
	return(t)

def rewind(file_name):
	"""change the read/write pointer  to the first line in the file you open"""
	file_name.seek(0)

def help_doc(function_module):
	"""this function is used to provide you with help_doc""" 
	print ("Help on function %s in module function") % function_module
	print (function_module.__doc__)

def reverse(li):
	"""reverse a list and return it""" 
	lj = []
	for i in range(0, len(li)):
		x = li.pop(-1)
		lj.append(x)
	return(lj)


def calculate():
	x = raw_input('Your number:')
	print "The answer is:",
	print x
	print "Do you want to continue?press CTRL+C to stop and press Enter to continue."
	y = raw_input('>>')
	calculate()

calculate()