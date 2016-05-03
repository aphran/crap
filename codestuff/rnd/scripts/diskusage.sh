#!/usr/bin/env bash
topn=20
files="$(du -a ${1} | sort -n -r | head -n ${topn})"
prevsize='none'
currsize=0
for file in "${files[@]}":
    currsize=$( echo ${file} | awk '{ print \$1 }' )
    if [ prevsize != 'none' ]; then
        if [ ${prevsize} -ne ${currsize} ]; then
            print "${file}"
        fi
    fi
    prevsize=${currsize}
