; ***************************************************************
; *                                                             *
; *  Column Update Subroutines for Constant-time Boxcar Filter  *
; *                                                             *
; ***************************************************************

	PUBLIC	__columnMove16
	.MODEL	FLAT

; The size of the column sums array must be rounded up to a multiple
; of 16 ints (64 bytes). There are no alignment restrictions.

; *******************************
; *                             *
; *  Stack Frame and Arguments  *
; *                             *
; *******************************

Args    STRUCT
saves   DWORD 3 dup (?)		; 2 saved registers plus return address
posRow  DWORD ?           ; address of leading source row to add to column sums
negRow  DWORD ?           ; address of training source row to subtract from column sums
colSums DWORD ?           ; address of column sums (32-bit)
words   DWORD ?           ; number of columns
Args    ENDS

        .CODE

__columnMove16:
        push	  ebx
        push    edi

; Fetch arguments
        mov     eax, [esp + Args.posRow]
        mov     ebx, [esp + Args.negRow]
        mov     edi, [esp + Args.colSums]
        mov     ecx, [esp + Args.words]

; Make addresses point at end of rows
        lea     eax, [eax + ecx*2]
        lea     ebx, [ebx + ecx*2]
        lea     edi, [edi + ecx*4]

; loop count
        neg     ecx

; Main loop
loop16:

; Fetch 8 16-bit leading and training pixels, and 8 32-bit column sums
        movdqu  xmm0, [eax + ecx*2]
        movdqu  xmm1, [ebx + ecx*2]
        movdqu  xmm2, [edi + ecx*4]
        movdqu  xmm3, [edi + ecx*4 + 16]

        psubw   xmm0, xmm1        ; subtract training from leading

; Convert 16-bit differences to 32-bit (signed). The punpck*wd instructions place
; the 16-bit word in the high 16 bits of the 32-bit doublewords of the destination
; registers. We don't care what ends up in the low 16-bits. We then arithmetic
; shift right 16 so that the 16-bit values are sign-extended in the 32-bit
; dwords.
        punpckhwd xmm1, xmm0
        punpcklwd xmm0, xmm0
        psrad   xmm0, 16
        psrad   xmm1, 16

; Update the column sums
        paddd   xmm2, xmm0
        paddd   xmm3, xmm1
        movdqu  [edi + ecx*4], xmm2
        movdqu  [edi + ecx*4 + 16], xmm3

; Loop control
        add     ecx, 8
        jl      loop16

; Restore saved registers and return
        pop     edi
	      pop	    ebx

	      ret

        END
