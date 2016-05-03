#!/usr/bin/env bash

st=$1

if [ -z $st ]; then
    echo "Please specify enable or disable as a positional parameter"
    exit 1
fi

id=$(xinput list | grep Synaptics | awk 'BEGIN { FS = "\t" } { print $2 }')

xinput $st ${id/#*=/}
