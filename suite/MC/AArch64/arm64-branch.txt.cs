# CS_ARCH_AARCH64, None, None
# This regression test file is new. The option flags could not be determined.
# LLVM uses the following mattr = []
0xc0 0x03 0x5f 0xd6 == ret
0x20 0x00 0x5f 0xd6 == ret x1
0xe0 0x03 0xbf 0xd6 == drps
0xe0 0x03 0x9f 0xd6 == eret
0xa0 0x00 0x1f 0xd6 == br  x5
0x20 0x01 0x3f 0xd6 == blr x9
0x0B 0x00 0x18 0x37 == tbnz	w11, #3, #0
0x20 0x00 0x20 0xd4 == brk   #0x1
0x41 0x00 0xa0 0xd4 == dcps1 #0x2
0x62 0x00 0xa0 0xd4 == dcps2 #0x3
0x83 0x00 0xa0 0xd4 == dcps3 #0x4
0xa0 0x00 0x40 0xd4 == hlt   #0x5
0xc2 0x00 0x00 0xd4 == hvc   #0x6
0xe3 0x00 0x00 0xd4 == smc   #0x7
0x01 0x01 0x00 0xd4 == svc   #0x8
0x07 0x00 0x00 0x14 == b #28
0x06 0x00 0x00 0x94 == bl #24
0xa1 0x00 0x00 0x54 == b.ne #20
0x80 0x00 0x08 0x36 == tbz w0, #1, #16
0xe1 0xff 0xf7 0x36 == tbz w1, #30, #-4
0x60 0x00 0x08 0x37 == tbnz w0, #1, #12
0x40 0x00 0x00 0xb4 == cbz x0, #8
0x20 0x00 0x00 0xb5 == cbnz x0, #4
0x1f 0x20 0x03 0xd5 == nop
0xff 0xff 0xff 0x17 == b #-4
0xc1 0xff 0xff 0x54 == b.ne #-8
0xa0 0xff 0x0f 0x36 == tbz w0, #1, #-12
0x80 0xff 0xff 0xb4 == cbz x0, #-16
0x1f 0x20 0x03 0xd5 == nop
