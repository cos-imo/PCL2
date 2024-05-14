
  ; appeler la fonction printf pour afficher
  mov rdi, format_X
  xor rsi, rsi
  movzx rsi, word <VALUE>
  xor rax, rax
  call printf


