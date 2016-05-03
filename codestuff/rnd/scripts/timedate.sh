#!/usr/bin/env bash
ww=$(echo $(($(date +%U) + 1)) $(date +%Y-%m-%d\ %H:%M:%S))
ts="WW$ww"
echo $ts
