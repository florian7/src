[SECTION .text]
global _start
_start:
	mov		bl, 255	; exit code
	mov		al, 1	; exit command to kernel
	int		0x80	; interrupt
