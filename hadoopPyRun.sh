#!/bin/bash
#usage: ./scriptName mapper reducer input output
#assume mapper reducer in current dir
#assume input in hdfs, otherwise in current dir
mapper=$(pwd)"/"$1
reducer=$(pwd)"/"$2
input_local=$(pwd)"/"$3
output_local=$(pwd)"/"$4
input_dir="/user/root/input/"
input_remote=$input_dir$3
output_remote="/user/root/output/"$4

echo mapper:$mapper
echo reducer:$reducer
echo input:$input_remote
echo output:$output_remote

hadoop fs -ls $input_remote &> /dev/null
if [ $? -eq 1 ];then
	hadoop fs -put $input_local $input_dir
fi
hadoop fs -rm -f -r $output_remote

hadoop jar /usr/local/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar -D mapred.reduce.tasks=5 -mapper "python $mapper" -reducer "python $reducer" -input "$input_remote" -output "$output_remote"

hadoop fs -getmerge $output_remote $output_local
