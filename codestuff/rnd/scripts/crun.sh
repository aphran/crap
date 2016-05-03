#/bin/sh

code=$1
out=runme

gcc $code -o $out
chmod +x $out
./$out
rm $out

