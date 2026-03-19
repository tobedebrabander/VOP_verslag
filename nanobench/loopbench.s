	.file	"loopbench.c"
	.text
	.globl	main
	.type	main, @function
main:
.LFB1:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movl	%edi, -52(%rbp)
	movq	%rsi, -64(%rbp)
	movl	$0, -4(%rbp)
	movq	$1, -16(%rbp)
#APP
# 9 "loopbench.c" 1
	mov -16(%rbp), %eax
	xchg %bx, %bx

# 0 "" 2
#NO_APP
	movq	%rax, -24(%rbp)
	movl	$0, -8(%rbp) #-8(%rbp) = i
	jmp	.L2
.L3:
	addl	$1, -4(%rbp) #-4(%rbp) = a
	addl	$1, -8(%rbp)
.L2:
	cmpl	$2, -8(%rbp)
	jle	.L3
	movq	$2, -32(%rbp)
#APP
# 13 "loopbench.c" 1
	mov -32(%rbp), %eax
	xchg %bx, %bx

# 0 "" 2
#NO_APP
	movq	%rax, -40(%rbp)
	movl	$0, %eax
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE1:
	.size	main, .-main
	.ident	"GCC: (Debian 14.2.0-19) 14.2.0"
	.section	.note.GNU-stack,"",@progbits
