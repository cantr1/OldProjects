.global _start
.intel_syntax noprefix

_start:
	// sys_write
	mov rax, 1
	mov rdi, 1
	lea rsi, [Hello_World]
	mov rdx, 14
	syscall

	// sys_exit
	mov rax, 60
	mov rdi, 69
	syscall

Hello_World:
	.asciz "Hello, World!\n"
