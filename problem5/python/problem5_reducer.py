#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys

PRINT_JSON = True

if PRINT_JSON:
    import json

    jenc = json.JSONEncoder()  # pylint: disable=C0103

strs = set()

for line in sys.stdin:
    line = line.strip()
    nucleotide, seqId = line.split('\t', 1)
    strs.add(nucleotide)

for item in strs:
    if PRINT_JSON:
        print(jenc.encode(item))
    else:
        print('%s' % item)
