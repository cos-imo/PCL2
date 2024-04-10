push ebp
mov ebp, esp
sub esp, <SIZE> ; remplacer size par la taille de la variable de retour
  ; code de la fonction ici
mov esp, ebp
pop ebp
