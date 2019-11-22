#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

PRINT_JSON = True

if PRINT_JSON:
    import json

    jenc = json.JSONEncoder()  # pylint: disable=C0103

who2friend = {}

for line in sys.stdin:
    line = line.strip()
    who, friend = line.split('\t', 1)
    if who not in who2friend:
        who2friend[who] = {friend}
    else:
        who2friend[who].add(friend)

for who in who2friend:
    if PRINT_JSON:
        print(jenc.encode((who, len(who2friend[who]))))
    else:
        print('%s\t%s' % (who, len(who2friend[who])))
