#!/bin/bash


evenFib() {
	limit=$1
	echo $limit
	let a=1
	let b=1
	let c=0
	let sum=0
	while [ $c -lt $limit ]; do
		let c=a+b
		let a=b
		let b=c
		if [ $[c % 2] -eq 0 ]; then
			let sum=sum+c
		fi	
	done
	echo $sum

}

evenFib 4000000
