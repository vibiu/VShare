#!usr/bin/python
# coding: utf-8

def cal(w):
    store = w.split('+')
    for i in range(0,len(store)):
        if '*' in store[i]:
            storeZ = store[i]
            store1 = storeZ.split('*')
            count = 1
            for t in store1:
                count = count * int(t)
            store[i] = count
            countMain = 0
        elif '/' in store[i]:
            storeZ = store[i]
            store1 = storeZ.split('/')
            count = float(store1[0]) / float(store1[1])
            store[i] = count
            countMain = 0   
        elif '-' in store[i]:
            storeZ = store[i]
            store1 = storeZ.split('-')
            if store1[0]:
                store[i] = int(store1[0]) - int(store1[1])
            else:
                store[i] = store[0] 
            countMain = 0
        else:
            pass
    countMain = 0
    for i in store:
        if i != '':
            countMain = countMain + float(i)
    return countMain
