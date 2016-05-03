# switch awesome theme

theme=$1

if [ -z $theme ]; then
    echo "Please specify a theme as a positional argument"
    exit 1
fi

# check theme files exist

rcd=~/.config/awesome
rct=$rcd/rc-$theme.lua
rcl=$rcd/rc.lua

if [ ! -f $rct ]; then
    echo "File '$rct' missing"
    exit 2
fi

xrd=~
xrl=$xrd/.Xresources
xrf=$xrl-$theme

if [ ! -f $xrf ]; then
    echo "File '$xrf' missing"
    exit 2
fi

# recreate awesome theme symlink
[ -f $rcl ] && rm $rcl
ln -s $rct $rcl

# recreate .Xresources symlink
[ -f $xrl ] && rm $xrl
ln -s $xrf $xrl
