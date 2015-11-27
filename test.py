# coding:utf-8

import calculator

express = [
    ("1+1", 2),
    ("1-1", 0),
    ("1*1", 1),
    ("-1+1", 0),
    ("1/1", 1),
    ("1", 1),
    ("+1", 1),
    ("-1", -1),
    ("0.33", 0.33),
    ("-1*1", -1),
    ("0*1", 0),
    ("0.5+0.5", 1.0),
    ("1/2", 0.5),
    ("-1/2", -0.5),
    ("0+0", 0),
    ("1+1*2", 3),
    ("1+2*2+3", 8),
    ("1+3/3+1", 3),
]


def test_cal():
    fail = 0
    for s, val in express:
        print "Expect: %s = %s" % (s, val)
        try:
            v = calculator.cal(s)
            if v != val:
                fail += 1
            status = "  OK  "if v == val else " Fail "
            print "%s: %s = %s" % (status, s, v)
        except Exception as ex:
            print "Exception: %s" % ex
    if fail == 0:
        print "Very good!!"
    else:
        print "Sorry: %spass, %sfail." % (len(express) - fail, fail)

if __name__ == '__main__':
    test_cal()
