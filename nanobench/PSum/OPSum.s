	.file	"OPSum.c"
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
	subq	$72, %rsp
	movl	%edi, -180(%rbp)
	movq	%rsi, -192(%rbp)
	movl	$1, -96(%rbp)
	movl	$0, -92(%rbp)
	movl	$0, -88(%rbp)
	movl	$0, -84(%rbp)
	movl	$1, -80(%rbp)
	movl	$1, -76(%rbp)
	movl	$0, -72(%rbp)
	movl	$1, -68(%rbp)
	movl	$0, -64(%rbp)
	movl	$1, -60(%rbp)
	movl	$1, -128(%rbp)
	movl	$2, -124(%rbp)
	movl	$3, -120(%rbp)
	movl	$4, -116(%rbp)
	movl	$5, -112(%rbp)
	movl	$0, -4(%rbp)
	movl	$0, -8(%rbp)
	movl	$0, -12(%rbp)
	movq	$1, -24(%rbp)
#APP
# 17 "OPSum.c" 1
	mov -24(%rbp), %eax
	xchg %bx, %bx

# 0 "" 2
#NO_APP
	movq	%rax, -32(%rbp)
	movl	$0, -8(%rbp)
	jmp	.L2
.L3:
	movl	-8(%rbp), %eax
	leal	(%rax,%rax), %ecx
	movslq	%ecx, %rax
	imulq	$1717986919, %rax, %rax
	shrq	$32, %rax
	movl	%eax, %edx
	sarl	%edx
	movl	%ecx, %eax
	sarl	$31, %eax
	subl	%eax, %edx
	movl	%edx, %eax
	sall	$2, %eax
	addl	%edx, %eax
	subl	%eax, %ecx
	movl	%ecx, %edx
	movl	-12(%rbp), %eax
	cltq
	movl	%edx, -176(%rbp,%rax,4)
	movl	-8(%rbp), %eax
	cltq
	movl	-96(%rbp,%rax,4), %eax
	addl	%eax, -12(%rbp)
	addl	$1, -8(%rbp)
.L2:
	cmpl	$9, -8(%rbp)
	jle	.L3
	movl	$0, -8(%rbp)
	jmp	.L4
.L5:
	movl	-8(%rbp), %eax
	cltq
	movl	-176(%rbp,%rax,4), %eax
	cltq
	movl	-128(%rbp,%rax,4), %eax
	addl	%eax, -4(%rbp)
	addl	$1, -8(%rbp)
.L4:
	movl	-8(%rbp), %eax
	cmpl	-12(%rbp), %eax
	jl	.L5
	movq	$2, -40(%rbp)
#APP
# 28 "OPSum.c" 1
	mov -40(%rbp), %eax
	xchg %bx, %bx

# 0 "" 2
#NO_APP
	movq	%rax, -48(%rbp)
	movl	$0, %eax
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE1:
	.size	main, .-main
	.ident	"GCC: (Debian 14.2.0-19) 14.2.0"
	.section	.note.GNU-stack,"",@progbits
