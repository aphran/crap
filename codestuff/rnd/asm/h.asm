section .text
global  _start      ;for linker ld

_start:             ;entry point
    mov edx,len     ;messg length
    mov ecx,msg     ;messg
    mov ebx,1       ;fd (stdout)
    mov eax,4       ;system call sys_write id
    int 0x80        ;call kernel

section .data

msg db  'hello world',0xa   ;string
len equ $ - msg             ;length of string
