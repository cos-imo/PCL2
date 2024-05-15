
  ; Début Put 
  mov rdi, format_X
  xor rsi, rsi
  movzx rsi, word <VALUE>
  xor rax, rax
  call printf
  ; Fin Put
