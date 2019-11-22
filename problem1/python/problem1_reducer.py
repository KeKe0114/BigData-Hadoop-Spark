#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
input: stdin
(word,filename) per line which can be parsed by str.split('\t', 1).
output: stdout
(word,filenames) per line formattd by JSONEncoder.
'''
import sys

PRINT_JSON = True

if PRINT_JSON:
    import json
    jenc = json.JSONEncoder()  # pylint: disable=C0103


word2file = {}  # pylint: disable=C0103

for line in sys.stdin:
    line = line.strip()
    word, filename = line.split('\t', 1)
    if word not in word2file:
        word2file[word] = {filename}
    else:
        word2file[word].add(filename)

for word, fileset in word2file.items():
    if PRINT_JSON:
        print(jenc.encode((word, [x for x in fileset])))
    else:
        print('%s\t%s' % (word, [x for x in fileset]))
