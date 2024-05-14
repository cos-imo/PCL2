
  ; appeler la fonction printf pour afficher l'entier 42
  mov rdi, format
  xor rsi, rsi
  movzx rsi, word <VALUE>
  xor rax, rax
  call printf

  mov eax, 60 ; code syscall pour terminer le programme
  xor edi, edi ; code de sortie 0
  syscall
