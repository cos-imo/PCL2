<FUNCTION_NAME>:
  push rbp
  mov rbp, rsp
  sub rsp, <RETURN_SIZE> ; remplacer size par la taille de la variable de retour
  
  ; code de la fonction
  <FUNCTION_CODE>
  
  mov rsp, rbp
  pop rbp
  ret
  
  <INSTRUCTION_BOUCLE>


