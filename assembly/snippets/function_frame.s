<FUNCTION_NAME>:
  push rbp
  mov rbp, rsp
  sub rsp, <SIZE> ; remplacer size par la taille de la variable de retour
  ; code de la fonction ici
  mov rsp, rbp
  pop rbp
  ret
