#
# ~/.bashrc
#

# Eternal bash history.
# ---------------------
# Undocumented feature which sets the size to "unlimited".
# http://stackoverflow.com/questions/9457233/unlimited-bash-history
export HISTFILESIZE=
export HISTSIZE=
export HISTTIMEFORMAT="[%F %T] "
# Change file location, certain bash sessions truncate .bash_history upon closure
# http://superuser.com/questions/575479/bash-history-truncated-to-500-lines-on-each-login
export HISTFILE=~/.bash_eternal_history
# Force prompt to write history after every command.
# http://superuser.com/questions/20900/bash-history-loss
#PROMPT_COMMAND="history -a; $PROMPT_COMMAND"

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# PS1 and colors already defined in /etc/bash.bashrc

# Aliases
if test -f $HOME/.aliases; then
  . $HOME/.aliases
fi

# Scripts
if test -d $HOME/scripts; then
  export PATH="$PATH:$HOME/scripts"
fi

# More PATH
export PATH="$PATH:/usr/lib/icecream/bin/"

# Proxy load already defined in /etc/bash.bashrc

# Directory colors
if test -f $HOME/.dircolors; then
  eval $(dircolors ~/.dircolors)
fi

# Powerline
if test -f $HOME/scripts/bash-powerline.sh; then
  . $HOME/scripts/bash-powerline.sh
fi
