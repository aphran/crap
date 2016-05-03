#!/usr/bin/env bash
printf "WW%02d\n" $(expr $(date +%U) + 1)
