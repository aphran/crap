#!/usr/bin/env bash

newlog=dirlog.new
oldlog=dirlog.old

while pwd >/dev/null; do
    ls /home/afxez0r/yocto/bugfix-envs/7664-empty-img/src/poky/build/tmp/sysroots/x86_64-linux/usr/bin/smart* > $newlog
    if [ -r $oldlog ]; then
        if $(diff $oldlog $newlog); then
            sleep 1
        else
            
        fi
    fi
done
