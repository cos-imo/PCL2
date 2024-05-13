mov dword [saved_eax], rax
mov dword [saved_ebx], rbx

pop rax
pop rbx
xor rdx, rdx
idiv rbx

mov dword [result], rax

mov rax, dword [saved_eax]
mov rbx, dword [saved_ebx]
