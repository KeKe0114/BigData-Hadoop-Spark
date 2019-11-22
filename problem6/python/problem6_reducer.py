#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import sys

PRINT_JSON = True

if PRINT_JSON:
    import json

    jenc = json.JSONEncoder()  # pylint: disable=C0103

pos2records = {}
# pos2records' key is (x, y); value is [records]

for line in sys.stdin:
    pos, record = line.strip().split('\t', 1)
    pos = eval(pos)
    pos2records.setdefault(pos, [])
    record = eval(record)
    pos2records[pos].append(record)

for pos, records in pos2records.items():
    a_row = list(filter(lambda x: x[0] == 'a', records))
    b_row = list(filter(lambda x: x[0] == 'b', records))

    result = 0
    for a in a_row:
        for b in b_row:
            if a[2] == b[1]:
                result += a[3] * b[3]

    if result != 0:
        if PRINT_JSON:
            print(jenc.encode(([pos[0], pos[1], result])))
        else:
            print([pos[0], pos[1], result])
