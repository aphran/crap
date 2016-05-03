#!/usr/bin/env python2

import ConfigParser, sys, os

for _,_, files in os.walk('.'):
    for f in [ _ for _ in files if _.endswith('.conf') and not _.startswith('yoctoAB') ]:
        n = f.split('.')[0]
        print("checking %s" % f)
        c = ConfigParser.ConfigParser()
        c.readfp(open(f))
        if (len(c.items(n)) > 0):
            print('[ OK ] %s parsed correctly' % n)
        else:
            print('[FAIL] %s did not parse' % n)
