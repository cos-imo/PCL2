begin_for_loop_X:
  mov R8, <var_indice_start>
  mov R9, <var_indice_stop>
  jmp for_loop_X
  ret

for_loop_X:
  cmp r8, r9
  je end_for_loop
  <FOR_LOOP_CODE_X>
  add r8, 1 
  jmp for_loop_X

end_for_loop:
  ret
