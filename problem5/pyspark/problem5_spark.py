#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import print_function
from pyspark import SparkContext
import json


sc = SparkContext( 'local', 'test')
textFile = sc.textFile("file:///home/root/SmallData/MP/problem5/dna.json")
dnas = textFile.map(lambda row: (json.loads(row)[1][:-10], 1)).reduceByKey(lambda a,b: a+b).map(lambda x:x[0])
dnas.foreach(print)
