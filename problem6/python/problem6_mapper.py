#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json

ISIZE, JSIZE = 11, 11

for line in sys.stdin:
    record = json.loads(line.strip())
    # record [matrix, i, j, value]
    if record[0] == 'a':
        i = record[1]
        for j in range(JSIZE):
            print('%s\t%s' % ((i, j), record))
    elif record[0] == 'b':
        j = record[2]
        for i in range(ISIZE):
            print('%s\t%s' % ((i, j), record))
