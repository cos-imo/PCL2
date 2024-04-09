mov dword [saved_eax], eax
mov dword [saved_ebx], ebx

pop eax
pop ebx
imul eax, ebx

mov dword [result], eax

mov eax, dword [saved_eax]
mov ebx, dword [saved_ebx]
