#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from pyspark import SparkContext
import json

def mapper(record):
    return (record[1], [record])  # (order_id, record)

def reducer(a, b):
    if b[0][0] == 'order':
        return b + a
    return a + b

def flatMapper(item):
    _ , values = item
    order = values[0]
    return zip([order]*len(values[1:]), values[1:])

sc = SparkContext( 'local', 'test')
textFile = sc.textFile("file:///home/root/SmallData/MP/problem2/records.json")
join = textFile.map(lambda row: json.loads(row)).map(mapper).reduceByKey(reducer).filter(lambda x: x[1][0][0]=='order').flatMap(flatMapper).map(lambda x:x[0]+x[1])
join.foreach(print)
