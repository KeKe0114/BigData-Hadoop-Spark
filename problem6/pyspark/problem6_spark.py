#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import print_function
from pyspark import SparkContext
import json

MAX_SIZE = 11

def flatMapper(item):
    if item[0] == 'a':
        return zip(zip([item[1]]*MAX_SIZE, range(MAX_SIZE)), [[item]]*MAX_SIZE)
    else:
        return zip(zip(range(MAX_SIZE), [item[2]]*MAX_SIZE), [[item]]*MAX_SIZE)


def mapper(item):
    key, values = item
    a_rows = filter(lambda x : x[0] == 'a', values)
    b_rows = filter(lambda x : x[0] == 'b', values)
    result = 0
    for a in a_rows:
        for b in b_rows:
            if (a[2]==b[1]):
                result += a[3] * b[3]
    return key, result

sc = SparkContext( 'local', 'test')
textFile = sc.textFile("file:///home/root/SmallData/MP/problem6/matrix.json")
point2value = textFile.map(lambda row: json.loads(row)).flatMap(flatMapper).reduceByKey(lambda a,b: a+b).map(mapper).filter(lambda x:x[1]>0)
point2value.foreach(print)

