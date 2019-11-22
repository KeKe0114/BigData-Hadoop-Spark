#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json

PRINT_JSON = True

if PRINT_JSON:
    import json
    jenc = json.JSONEncoder()  # pylint: disable=C0103

id2records = {}

for line in sys.stdin:
    line = line.strip()
    order_id, line = line.split('\t', 1)
    id2records.setdefault(order_id, [""])
    record = json.loads(line)
    if record[0] == 'order':
        id2records[order_id][0] = record
    elif record[0] == 'line_item':
        id2records[order_id].append(record)

for key, item in id2records.items():
    if item[0] and len(item)>1:
        for line_item in item[1:]:
            if PRINT_JSON:
                print(jenc.encode((item[0] + line_item)))
            else:
                print(item[0] + line_item)
