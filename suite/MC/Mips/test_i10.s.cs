# CS_ARCH_MIPS, CS_MODE_MIPS32+CS_MODE_BIG_ENDIAN, None

0x7b,0x06,0x32,0x07 == ldi.b   $w8, 198                # encoding: [0x7b,0x06,0x32,0x07]
0x7b,0x29,0xcd,0x07 == ldi.h   $w20, 313               # encoding: [0x7b,0x29,0xcd,0x07]
0x7b,0x4f,0x66,0x07 == ldi.w   $w24, 492               # encoding: [0x7b,0x4f,0x66,0x07]
0x7b,0x7a,0x66,0xc7 == ldi.d   $w27, -180              # encoding: [0x7b,0x7a,0x66,0xc7]
