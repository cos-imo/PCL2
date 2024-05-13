    ; Sauvegarde les registres utilisés
    mov dword [saved_eax], rax
    mov dword [saved_ebx], rbx

    ; Charge les valeurs des opérandes dans les registres
    mov rax, dword [<OP1>]   ; Charge la première opérande (op1) dans rax
    mov rbx, dword [<OP2>]   ; Charge la deuxième opérande (op2) dans rbx

    ; Effectue l'addition
    add rax, rbx

    ; Stocke le résultat dans la variable résultat
    mov dword [<RESULT>], rax

    ; Restaure les valeurs des registres
    mov rax, dword [saved_eax]
    mov rbx, dword [saved_ebx]
