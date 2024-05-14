  ; calcul du reste de la division euclidienne (modulo)
  mov ax, <VALUE1>   ; Charger le dividende dans ax
  cwd                ; Signe-étendre ax dans dx:ax
  mov bx, <VALUE2>   ; Charger le diviseur dans bx
  idiv bx            ; Diviser dx:ax par bx, quotient dans ax, reste dans dx
  mov [<RESULT>], dx ; Stocker le reste dans result
  ; fin du calcul du reste
