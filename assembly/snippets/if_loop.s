if_loop_X:
  <IF_CODE>
  cmp R8, 1
  jeq if_loop_X_true
  jne if_loop_X_false

if_loop_X_true:
  <IF_TRUE_CODE_X>
  jmp back_if_loop_X

if_loop_X_false:
  <IF_FALSE_CODE_X>
  jmp back_if_loop_X
