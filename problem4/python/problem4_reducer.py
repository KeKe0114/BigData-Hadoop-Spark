#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

PRINT_JSON = True

if PRINT_JSON:
    import json
    jenc = json.JSONEncoder()  # pylint: disable=C0103

person2friend = {}

for line in sys.stdin:
    line = line.strip()
    record = str(line).split('\t', 1)
    person2friend.setdefault(record[0], {})
    person2friend[record[0]].setdefault(record[1], 0)
    person2friend[record[0]][record[1]] = person2friend[record[0]][record[1]] + 1

for person, friends in person2friend.items():
    for friend, count in friends.items():
        if count == 1:
            if PRINT_JSON:
                print(jenc.encode((person, friend)))
            else:
                print('%s\t%s' % (person, friend))
