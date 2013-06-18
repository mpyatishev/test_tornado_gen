#!/bin/sh

count=5
i=1
while [ $i -le $count ]
do
	echo $i
	python3.2 test_async.py
	i=$(expr $i + 1)
done
