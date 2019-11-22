#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
input: record file.
every line is formatted to be (filename,file content)
so that can be parse by json.

output: into stdout.
(word,filename) delimiter is \t.
so that can be parse by str.split('\t', 1)
'''
import sys
import json

for line in sys.stdin:
    line = line.strip()
    record = json.loads(line)
    key = record[0]
    value = record[1]
    words = value.split()
    for word in words:
        print('%s\t%s' % (word, key))
