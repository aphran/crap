" Modified on 2016-01-20

syntax on
filetype on

set autoread
set magic
set number
set numberwidth=1
set ruler
set smarttab
"set ai " Auto  indent
"set si " Smart indent
set tabstop=4
set shiftwidth=4
set expandtab
set nowritebackup
set noswapfile
set bufhidden=unload
set history=128
set pastetoggle=<F2>
set nopaste
set nocompatible
"set backspace=eol,start,indent
"set backspace=2
set showmode
set hlsearch
set statusline+=%F
set laststatus=2

"colorscheme delek
"colorscheme github
colorscheme vlight

" Highlighting extras
" list with: ls -1 $(find /usr -type d -iname ftplugin 2>/dev/null)
au BufRead,BufNewFile *.pc set filetype=c
au BufRead,BufNewFile *.bbclass set filetype=python
au BufRead,BufNewFile *.bb set filetype=sh
au BufRead,BufNewFile *.profile set filetype=conf
