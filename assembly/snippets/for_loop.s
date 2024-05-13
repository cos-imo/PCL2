begin_for_loop_X:
  mov r8d, <var_indice_start>
  mov r9d, <var_indice_stop>
  jmp for_loop_X

for_loop_X:
  cmp r8d, r9d
  jg end_for_loop ; Saute hors de la boucle si r8d > r9d
  <FOR_LOOP_CODE_X>
  add r8d, 1 
  jmp for_loop_X

end_for_loop:
  mov rsp, rbp
  pop rbp
  ret
