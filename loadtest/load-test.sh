#!/bin/bash
set -o pipefail
max="$1"
date
echo "url: $2
rate: ${max} calls / second"
START=$(date +%s)

get() {
	request_time=$(date +'%r')
	curl -s -v -o /dev/null -w "%{http_code}\n" "$1" 2> >(tr '\r\n' '\\n' | awk -v date="${request_time}" '{print $0"\n-----", date}' >>/tmp/perf-test.log)
}

while true; do
	current_time=$(date +%s)
	echo $((current_time - START)) | awk '{print int($1/60)":"int($1%60)}'
	sleep 1

	for ((i = 1; i <= max; i++)); do
		get "$2" &
	done
done
