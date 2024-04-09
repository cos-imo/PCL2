section .data
    saved_eax dd 0
    saved_ebx dd 0
    result dd 0

section .text
    global _start

_start:
    mov dword [saved_eax], eax
    mov dword [saved_ebx], ebx

    pop eax
    pop ebx
    add eax, ebx

    mov dword [result], eax

    mov eax, dword [saved_eax]
    mov ebx, dword [saved_ebx]

    mov eax, 1
    xor ebx, ebx
    int 0x80
