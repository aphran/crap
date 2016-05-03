#!/usr/bin/env bash

# Some dummy multi-line content
read -d '' colours <<- 'EOF'
	red
	green
	blue
EOF

# File descriptor 3 produces colours
exec 3< <(echo "$colours")

# File descriptor 4 filters colours
exec 4> >(grep --color=never green)

# File descriptor 5 is an unlimited supply of violet
exec 5< <(yes violet)

echo Reading colours from file descriptor 3...
cat <&3
echo ... done.

echo Reading colours from file descriptor 3 again...
cat <&3
echo ... done.

echo Filtering colours through file descriptor 4...
echo "$colours" >&4
echo ... done. # Race condition?

echo Dipping into some violet...
head <&5
echo ... done.

echo Dipping into some more violet...
head <&5
echo ... done.
