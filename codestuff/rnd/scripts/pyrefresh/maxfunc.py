#!/usr/bin/env python2

func_len = 2
powa = 2

while True:
    _func_name = 'a' * func_len
    print "%s" % str(func_len)
    exec "def %s(): pass" % _func_name
    exec "%s()" % _func_name
    func_len = func_len**powa
