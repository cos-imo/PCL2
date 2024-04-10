push ebp
mov ebp, esp
sub esp, f"{size}" . ; remplacer size par la taille de la variable de retour
  ; code de la fonction ici
mov esp, ebp
pop ebp
