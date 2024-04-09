section .data
  ; data section

section .text
    global _start

_start:

  ; code

  ; exiting program
    mov eax, 1
    xor ebx, ebx
    int 0x80
