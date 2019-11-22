#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json

for line in sys.stdin:
    line = line.strip()
    record = json.loads(line)
    order_id = record[1]
    print('%s\t%s' % (order_id, line))
