mov dword [saved_eax], rax
mov dword [saved_ebx], rbx

pop rax
pop rbx
imul rax, rbx

mov dword [result], rax

mov rax, dword [saved_eax]
mov rbx, dword [saved_ebx]
