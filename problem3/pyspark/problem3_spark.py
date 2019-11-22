#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import print_function
from pyspark import SparkContext
import json
sc = SparkContext( 'local', 'test')
textFile = sc.textFile("file:///home/root/SmallData/MP/problem3/friends.json")
friendsCount = textFile.map(lambda row:json.loads(row)[0]).map(lambda who: (who, 1)).reduceByKey(lambda a,b:a+b)
friendsCount.foreach(print)
