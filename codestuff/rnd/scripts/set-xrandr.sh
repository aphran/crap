#!/usr/bin/env bash

# Displays

# List of connected interfaces
conns=($(xrandr | egrep ' connected ' | cut -d' ' -f1))
# Disconnected interfaces
discs=($(xrandr | egrep 'disconnected [0-9]+x[0-9]+' | cut -d' ' -f1))

echo -e "connected:\n${conns[@]}"
echo -e "active disconnected:\n${discs[@]}"

# Main laptop display
MAIN="eDP1"
MODE="1920x1080"

# Office screens
OS1="DP2-2"
OS2="DP2-3"

# Home screens
# tbd

# Projector(s)
PRJ="VGA1"

cmd="/usr/bin/xrandr"

$cmd --output $MAIN --mode $MODE --pos 0x0

# First off, deactivate all disconnected screens that are active
for disp in "${discs[@]}"; do
    $cmd --output $disp --off
done

# Main config, both office screens connected:
if [[ " ${conns[@]} " =~ " ${OS1} " ]] && \
   [[ " ${conns[@]} " =~ " ${OS2} " ]]; then
    # Deactivate VGA (whether connected or not)
    $cmd --output $PRJ --off
    # Activate both screens
    $cmd --output $OS1 --auto  --same-as $MAIN
    $cmd --output $OS2 --auto --right-of $MAIN
else
    # Configure projectors
    if [[ " ${conns[@]} " =~ " ${PRJ} " ]]; then # prj connected
        $cmd --output $PRJ --auto --left-of $MAIN
    fi
    # Both screens aren't connected (but either might)
    if [[ " ${conns[@]} " =~ " ${OS1} " ]]; then # scr 1 connected
        $cmd --output $OS2 --off
        $cmd --output $OS1 --auto --right-of $MAIN
    elif [[ " ${conns[@]} " =~ " ${OS2} " ]]; then # scr 2 connected
        $cmd --output $OS1 --off
        $cmd --output $OS2 --auto --right-of $MAIN
    fi
fi

# Configure home (non-dock) screens:
# tbd


