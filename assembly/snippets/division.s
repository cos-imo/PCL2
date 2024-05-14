  
    
; division
mov ax, <VALUE1>   ; Charger le dividende dans ax
cwd                
mov bx, <VALUE2>   ; Charger le diviseur dans bx
idiv bx            ; Diviser dx:ax par bx, quotient dans ax, reste dans dx
mov [<RESULT>], ax 
; fin division




