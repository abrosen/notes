#!/bin/bash
a=3
b=5
limit=1000
sum=0
echo $a $b $limit
i=1
while [ $i -lt $limit ] ; do
	if [ $[i % a] -eq 0 -o $[i % b] -eq 0 ] ; then
		let sum=sum+i
	fi
	let i=i+1
done
echo $sum
	       	
