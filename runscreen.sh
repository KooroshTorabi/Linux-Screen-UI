#!/bin/sh

log_dir=$(awk -F '=' '/\[main\]/{a=1}a==1&&$1~/log_dir/{print $2;exit}' config.ini)

if [ ! -d $log_dir -a ! -h "" ]
then
	mkdir $log_dir
fi 

file_name=$(date +"%Y-%m-%d_%H-%M-%S")
timing_file="./"$log_dir"/"$file_name".timing"
log_file="./"$log_dir"/"$file_name".log"

script --timing=$timing_file $log_file -q