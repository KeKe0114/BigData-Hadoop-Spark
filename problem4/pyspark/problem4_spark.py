#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import print_function
from pyspark import SparkContext
import json


sc = SparkContext( 'local', 'test')
textFile = sc.textFile("file:///home/root/SmallData/MP/problem4/friends.json")
friendsAsymmetric = textFile.map(lambda row: json.loads(row)).flatMap(lambda x: (((x[0],x[1]),1), ((x[1],x[0]),1)) ).reduceByKey(lambda a,b:a+b).filter(lambda x:x[1]<2).map(lambda x:x[0])
friendsAsymmetric.foreach(print) 
