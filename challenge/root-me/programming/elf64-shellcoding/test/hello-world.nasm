[SECTION .text]

global _start

_start:
	
	jmp short ender

	starter:

	xor eax, eax
	xor ebx, ebx
	xor ecx, ecx
	xor edx, edx

	mov al, 4		;system call
	mov bl, 1		;stdout
	pop ecx			;pop out string address from stack
	mov dl, 18		;string length
	int 0x80		;call

	xor eax, eax
	xor ebx, ebx

	mov al, 1		;exit call
	int 0x80		;call

	ender:
	call starter	;put string address on stack
	db 'Hello Motherfucker'

