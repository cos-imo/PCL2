section .data
  ; data section

section .text
    global _start

_start:
  ; code

  ; exiting program
  mov rax, 1
  xor rbx, rbx
  int 0x80
