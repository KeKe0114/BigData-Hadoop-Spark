#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from pyspark import SparkContext
import json

def mapper(item):
    key, values = item
    values = values.split()
    return zip(values, [{key}]*len(values))

sc = SparkContext('local', 'test')
textFile = sc.textFile("file:///home/root/SmallData/MP/problem1/books.json")

invert_index = textFile.map(lambda row: json.loads(row)).flatMap(mapper).reduceByKey(lambda a,b:set.union(a,b)).map(lambda x: (x[0],list(x[1])))
invert_index.foreach(print)
