from . import CS_OP_INVALID, CS_OP_REG, CS_OP_IMM, CS_OP_FP, CS_OP_PRED, CS_OP_SPECIAL, CS_OP_MEM, CS_OP_MEM_REG, CS_OP_MEM_IMM, UINT16_MAX, UINT8_MAX
# For Capstone Engine. AUTO-GENERATED FILE, DO NOT EDIT [arm_const.py]

ARMCC_EQ = 0
ARMCC_NE = 1
ARMCC_HS = 2
ARMCC_LO = 3
ARMCC_MI = 4
ARMCC_PL = 5
ARMCC_VS = 6
ARMCC_VC = 7
ARMCC_HI = 8
ARMCC_LS = 9
ARMCC_GE = 10
ARMCC_LT = 11
ARMCC_GT = 12
ARMCC_LE = 13
ARMCC_AL = 14
ARMCC_UNDEF = 15

ARMVCC_None = 0
ARMVCC_Then = 1
ARMVCC_Else = 2

ARM_PredBlockMaskInvalid = 0
ARM_T = 0x8
ARM_TT = 0x4
ARM_TE = 0xc
ARM_TTT = 0x2
ARM_TTE = 0x6
ARM_TEE = 0xe
ARM_TET = 0xa
ARM_TTTT = 0x1
ARM_TTTE = 0x3
ARM_TTEE = 0x7
ARM_TTET = 0x5
ARM_TEEE = 0xf
ARM_TEET = 0xd
ARM_TETT = 0x9
ARM_TETE = 0xb

ARM_SFT_INVALID = 0
ARM_SFT_ASR = 1
ARM_SFT_LSL = 2
ARM_SFT_LSR = 3
ARM_SFT_ROR = 4
ARM_SFT_RRX = 5
ARM_SFT_UXTW = 6
ARM_SFT_REG = 7
ARM_SFT_ASR_REG = 8
ARM_SFT_LSL_REG = 9
ARM_SFT_LSR_REG = 10
ARM_SFT_ROR_REG = 11

ARM_MB_RESERVED_0 = 0
ARM_MB_OSHLD = 1
ARM_MB_OSHST = 2
ARM_MB_OSH = 3
ARM_MB_RESERVED_4 = 4
ARM_MB_NSHLD = 5
ARM_MB_NSHST = 6
ARM_MB_NSH = 7
ARM_MB_RESERVED_8 = 8
ARM_MB_ISHLD = 9
ARM_MB_ISHST = 10
ARM_MB_ISH = 11
ARM_MB_RESERVED_12 = 12
ARM_MB_LD = 13
ARM_MB_ST = 14
ARM_MB_SY = 15
ARM_FIELD_SPSR_C = 1
ARM_FIELD_SPSR_X = 2
ARM_FIELD_SPSR_S = 4
ARM_FIELD_SPSR_F = 8
ARM_FIELD_CPSR_C = 16
ARM_FIELD_CPSR_X = 32
ARM_FIELD_CPSR_S = 64
ARM_FIELD_CPSR_F = 128
ARM_BANKEDREG_ELR_HYP = 0x1e
ARM_BANKEDREG_LR_ABT = 0x14
ARM_BANKEDREG_LR_FIQ = 0xe
ARM_BANKEDREG_LR_IRQ = 0x10
ARM_BANKEDREG_LR_MON = 0x1c
ARM_BANKEDREG_LR_SVC = 0x12
ARM_BANKEDREG_LR_UND = 0x16
ARM_BANKEDREG_LR_USR = 0x6
ARM_BANKEDREG_R10_FIQ = 0xa
ARM_BANKEDREG_R10_USR = 0x2
ARM_BANKEDREG_R11_FIQ = 0xb
ARM_BANKEDREG_R11_USR = 0x3
ARM_BANKEDREG_R12_FIQ = 0xc
ARM_BANKEDREG_R12_USR = 0x4
ARM_BANKEDREG_R8_FIQ = 0x8
ARM_BANKEDREG_R8_USR = 0x0
ARM_BANKEDREG_R9_FIQ = 0x9
ARM_BANKEDREG_R9_USR = 0x1
ARM_BANKEDREG_SPSR_ABT = 0x34
ARM_BANKEDREG_SPSR_FIQ = 0x2e
ARM_BANKEDREG_SPSR_HYP = 0x3e
ARM_BANKEDREG_SPSR_IRQ = 0x30
ARM_BANKEDREG_SPSR_MON = 0x3c
ARM_BANKEDREG_SPSR_SVC = 0x32
ARM_BANKEDREG_SPSR_UND = 0x36
ARM_BANKEDREG_SP_ABT = 0x15
ARM_BANKEDREG_SP_FIQ = 0xd
ARM_BANKEDREG_SP_HYP = 0x1f
ARM_BANKEDREG_SP_IRQ = 0x11
ARM_BANKEDREG_SP_MON = 0x1d
ARM_BANKEDREG_SP_SVC = 0x13
ARM_BANKEDREG_SP_UND = 0x17
ARM_BANKEDREG_SP_USR = 0x5
ARM_MCLASSSYSREG_APSR = 0x800
ARM_MCLASSSYSREG_APSR_G = 0x400
ARM_MCLASSSYSREG_APSR_NZCVQ = 0x800
ARM_MCLASSSYSREG_APSR_NZCVQG = 0xc00
ARM_MCLASSSYSREG_BASEPRI = 0x811
ARM_MCLASSSYSREG_BASEPRI_MAX = 0x812
ARM_MCLASSSYSREG_BASEPRI_NS = 0x891
ARM_MCLASSSYSREG_CONTROL = 0x814
ARM_MCLASSSYSREG_CONTROL_NS = 0x894
ARM_MCLASSSYSREG_EAPSR = 0x802
ARM_MCLASSSYSREG_EAPSR_G = 0x402
ARM_MCLASSSYSREG_EAPSR_NZCVQ = 0x802
ARM_MCLASSSYSREG_EAPSR_NZCVQG = 0xc02
ARM_MCLASSSYSREG_EPSR = 0x806
ARM_MCLASSSYSREG_FAULTMASK = 0x813
ARM_MCLASSSYSREG_FAULTMASK_NS = 0x893
ARM_MCLASSSYSREG_IAPSR = 0x801
ARM_MCLASSSYSREG_IAPSR_G = 0x401
ARM_MCLASSSYSREG_IAPSR_NZCVQ = 0x801
ARM_MCLASSSYSREG_IAPSR_NZCVQG = 0xc01
ARM_MCLASSSYSREG_IEPSR = 0x807
ARM_MCLASSSYSREG_IPSR = 0x805
ARM_MCLASSSYSREG_MSP = 0x808
ARM_MCLASSSYSREG_MSPLIM = 0x80a
ARM_MCLASSSYSREG_MSPLIM_NS = 0x88a
ARM_MCLASSSYSREG_MSP_NS = 0x888
ARM_MCLASSSYSREG_PAC_KEY_P_0 = 0x820
ARM_MCLASSSYSREG_PAC_KEY_P_0_NS = 0x8a0
ARM_MCLASSSYSREG_PAC_KEY_P_1 = 0x821
ARM_MCLASSSYSREG_PAC_KEY_P_1_NS = 0x8a1
ARM_MCLASSSYSREG_PAC_KEY_P_2 = 0x822
ARM_MCLASSSYSREG_PAC_KEY_P_2_NS = 0x8a2
ARM_MCLASSSYSREG_PAC_KEY_P_3 = 0x823
ARM_MCLASSSYSREG_PAC_KEY_P_3_NS = 0x8a3
ARM_MCLASSSYSREG_PAC_KEY_U_0 = 0x824
ARM_MCLASSSYSREG_PAC_KEY_U_0_NS = 0x8a4
ARM_MCLASSSYSREG_PAC_KEY_U_1 = 0x825
ARM_MCLASSSYSREG_PAC_KEY_U_1_NS = 0x8a5
ARM_MCLASSSYSREG_PAC_KEY_U_2 = 0x826
ARM_MCLASSSYSREG_PAC_KEY_U_2_NS = 0x8a6
ARM_MCLASSSYSREG_PAC_KEY_U_3 = 0x827
ARM_MCLASSSYSREG_PAC_KEY_U_3_NS = 0x8a7
ARM_MCLASSSYSREG_PRIMASK = 0x810
ARM_MCLASSSYSREG_PRIMASK_NS = 0x890
ARM_MCLASSSYSREG_PSP = 0x809
ARM_MCLASSSYSREG_PSPLIM = 0x80b
ARM_MCLASSSYSREG_PSPLIM_NS = 0x88b
ARM_MCLASSSYSREG_PSP_NS = 0x889
ARM_MCLASSSYSREG_SP_NS = 0x898
ARM_MCLASSSYSREG_XPSR = 0x803
ARM_MCLASSSYSREG_XPSR_G = 0x403
ARM_MCLASSSYSREG_XPSR_NZCVQ = 0x803
ARM_MCLASSSYSREG_XPSR_NZCVQG = 0xc03
ARM_OP_INVALID = CS_OP_INVALID
ARM_OP_REG = CS_OP_REG
ARM_OP_IMM = CS_OP_IMM
ARM_OP_FP = CS_OP_FP
ARM_OP_PRED = CS_OP_PRED
ARM_OP_CIMM = CS_OP_SPECIAL+0
ARM_OP_PIMM = CS_OP_SPECIAL+1
ARM_OP_SETEND = CS_OP_SPECIAL+2
ARM_OP_SYSREG = CS_OP_SPECIAL+3
ARM_OP_BANKEDREG = CS_OP_SPECIAL+4
ARM_OP_SPSR = CS_OP_SPECIAL+5
ARM_OP_CPSR = CS_OP_SPECIAL+6
ARM_OP_SYSM = CS_OP_SPECIAL+7
ARM_OP_VPRED_R = CS_OP_SPECIAL+8
ARM_OP_VPRED_N = CS_OP_SPECIAL+9
ARM_OP_MEM = CS_OP_MEM

ARM_SETEND_INVALID = 0
ARM_SETEND_BE = 1
ARM_SETEND_LE = 2

ARM_CPSMODE_INVALID = 0
ARM_CPSMODE_IE = 2
ARM_CPSMODE_ID = 3

ARM_CPSFLAG_INVALID = 0
ARM_CPSFLAG_F = 1
ARM_CPSFLAG_I = 2
ARM_CPSFLAG_A = 4
ARM_CPSFLAG_NONE = 16

ARM_VECTORDATA_INVALID = 0
ARM_VECTORDATA_I8 = 1
ARM_VECTORDATA_I16 = 2
ARM_VECTORDATA_I32 = 3
ARM_VECTORDATA_I64 = 4
ARM_VECTORDATA_S8 = 5
ARM_VECTORDATA_S16 = 6
ARM_VECTORDATA_S32 = 7
ARM_VECTORDATA_S64 = 8
ARM_VECTORDATA_U8 = 9
ARM_VECTORDATA_U16 = 10
ARM_VECTORDATA_U32 = 11
ARM_VECTORDATA_U64 = 12
ARM_VECTORDATA_P8 = 13
ARM_VECTORDATA_P16 = 14
ARM_VECTORDATA_F16 = 15
ARM_VECTORDATA_F32 = 16
ARM_VECTORDATA_F64 = 17
ARM_VECTORDATA_F16F64 = 18
ARM_VECTORDATA_F64F16 = 19
ARM_VECTORDATA_F32F16 = 20
ARM_VECTORDATA_F16F32 = 21
ARM_VECTORDATA_F64F32 = 22
ARM_VECTORDATA_F32F64 = 23
ARM_VECTORDATA_S32F32 = 24
ARM_VECTORDATA_U32F32 = 25
ARM_VECTORDATA_F32S32 = 26
ARM_VECTORDATA_F32U32 = 27
ARM_VECTORDATA_F64S16 = 28
ARM_VECTORDATA_F32S16 = 29
ARM_VECTORDATA_F64S32 = 30
ARM_VECTORDATA_S16F64 = 31
ARM_VECTORDATA_S16F32 = 32
ARM_VECTORDATA_S32F64 = 33
ARM_VECTORDATA_U16F64 = 34
ARM_VECTORDATA_U16F32 = 35
ARM_VECTORDATA_U32F64 = 36
ARM_VECTORDATA_F64U16 = 37
ARM_VECTORDATA_F32U16 = 38
ARM_VECTORDATA_F64U32 = 39
ARM_VECTORDATA_F16U16 = 40
ARM_VECTORDATA_U16F16 = 41
ARM_VECTORDATA_F16U32 = 42
ARM_VECTORDATA_U32F16 = 43
ARM_VECTORDATA_F16S16 = 44
ARM_VECTORDATA_S16F16 = 45
ARM_VECTORDATA_F16S32 = 46
ARM_VECTORDATA_S32F16 = 47

ARM_REG_INVALID = 0
ARM_REG_APSR = 1
ARM_REG_APSR_NZCV = 2
ARM_REG_CPSR = 3
ARM_REG_FPCXTNS = 4
ARM_REG_FPCXTS = 5
ARM_REG_FPEXC = 6
ARM_REG_FPINST = 7
ARM_REG_FPSCR = 8
ARM_REG_FPSCR_NZCV = 9
ARM_REG_FPSCR_NZCVQC = 10
ARM_REG_FPSID = 11
ARM_REG_ITSTATE = 12
ARM_REG_LR = 13
ARM_REG_PC = 14
ARM_REG_RA_AUTH_CODE = 15
ARM_REG_SP = 16
ARM_REG_SPSR = 17
ARM_REG_VPR = 18
ARM_REG_ZR = 19
ARM_REG_D0 = 20
ARM_REG_D1 = 21
ARM_REG_D2 = 22
ARM_REG_D3 = 23
ARM_REG_D4 = 24
ARM_REG_D5 = 25
ARM_REG_D6 = 26
ARM_REG_D7 = 27
ARM_REG_D8 = 28
ARM_REG_D9 = 29
ARM_REG_D10 = 30
ARM_REG_D11 = 31
ARM_REG_D12 = 32
ARM_REG_D13 = 33
ARM_REG_D14 = 34
ARM_REG_D15 = 35
ARM_REG_D16 = 36
ARM_REG_D17 = 37
ARM_REG_D18 = 38
ARM_REG_D19 = 39
ARM_REG_D20 = 40
ARM_REG_D21 = 41
ARM_REG_D22 = 42
ARM_REG_D23 = 43
ARM_REG_D24 = 44
ARM_REG_D25 = 45
ARM_REG_D26 = 46
ARM_REG_D27 = 47
ARM_REG_D28 = 48
ARM_REG_D29 = 49
ARM_REG_D30 = 50
ARM_REG_D31 = 51
ARM_REG_FPINST2 = 52
ARM_REG_MVFR0 = 53
ARM_REG_MVFR1 = 54
ARM_REG_MVFR2 = 55
ARM_REG_P0 = 56
ARM_REG_Q0 = 57
ARM_REG_Q1 = 58
ARM_REG_Q2 = 59
ARM_REG_Q3 = 60
ARM_REG_Q4 = 61
ARM_REG_Q5 = 62
ARM_REG_Q6 = 63
ARM_REG_Q7 = 64
ARM_REG_Q8 = 65
ARM_REG_Q9 = 66
ARM_REG_Q10 = 67
ARM_REG_Q11 = 68
ARM_REG_Q12 = 69
ARM_REG_Q13 = 70
ARM_REG_Q14 = 71
ARM_REG_Q15 = 72
ARM_REG_R0 = 73
ARM_REG_R1 = 74
ARM_REG_R2 = 75
ARM_REG_R3 = 76
ARM_REG_R4 = 77
ARM_REG_R5 = 78
ARM_REG_R6 = 79
ARM_REG_R7 = 80
ARM_REG_R8 = 81
ARM_REG_R9 = 82
ARM_REG_R10 = 83
ARM_REG_R11 = 84
ARM_REG_R12 = 85
ARM_REG_S0 = 86
ARM_REG_S1 = 87
ARM_REG_S2 = 88
ARM_REG_S3 = 89
ARM_REG_S4 = 90
ARM_REG_S5 = 91
ARM_REG_S6 = 92
ARM_REG_S7 = 93
ARM_REG_S8 = 94
ARM_REG_S9 = 95
ARM_REG_S10 = 96
ARM_REG_S11 = 97
ARM_REG_S12 = 98
ARM_REG_S13 = 99
ARM_REG_S14 = 100
ARM_REG_S15 = 101
ARM_REG_S16 = 102
ARM_REG_S17 = 103
ARM_REG_S18 = 104
ARM_REG_S19 = 105
ARM_REG_S20 = 106
ARM_REG_S21 = 107
ARM_REG_S22 = 108
ARM_REG_S23 = 109
ARM_REG_S24 = 110
ARM_REG_S25 = 111
ARM_REG_S26 = 112
ARM_REG_S27 = 113
ARM_REG_S28 = 114
ARM_REG_S29 = 115
ARM_REG_S30 = 116
ARM_REG_S31 = 117
ARM_REG_D0_D2 = 118
ARM_REG_D1_D3 = 119
ARM_REG_D2_D4 = 120
ARM_REG_D3_D5 = 121
ARM_REG_D4_D6 = 122
ARM_REG_D5_D7 = 123
ARM_REG_D6_D8 = 124
ARM_REG_D7_D9 = 125
ARM_REG_D8_D10 = 126
ARM_REG_D9_D11 = 127
ARM_REG_D10_D12 = 128
ARM_REG_D11_D13 = 129
ARM_REG_D12_D14 = 130
ARM_REG_D13_D15 = 131
ARM_REG_D14_D16 = 132
ARM_REG_D15_D17 = 133
ARM_REG_D16_D18 = 134
ARM_REG_D17_D19 = 135
ARM_REG_D18_D20 = 136
ARM_REG_D19_D21 = 137
ARM_REG_D20_D22 = 138
ARM_REG_D21_D23 = 139
ARM_REG_D22_D24 = 140
ARM_REG_D23_D25 = 141
ARM_REG_D24_D26 = 142
ARM_REG_D25_D27 = 143
ARM_REG_D26_D28 = 144
ARM_REG_D27_D29 = 145
ARM_REG_D28_D30 = 146
ARM_REG_D29_D31 = 147
ARM_REG_Q0_Q1 = 148
ARM_REG_Q1_Q2 = 149
ARM_REG_Q2_Q3 = 150
ARM_REG_Q3_Q4 = 151
ARM_REG_Q4_Q5 = 152
ARM_REG_Q5_Q6 = 153
ARM_REG_Q6_Q7 = 154
ARM_REG_Q7_Q8 = 155
ARM_REG_Q8_Q9 = 156
ARM_REG_Q9_Q10 = 157
ARM_REG_Q10_Q11 = 158
ARM_REG_Q11_Q12 = 159
ARM_REG_Q12_Q13 = 160
ARM_REG_Q13_Q14 = 161
ARM_REG_Q14_Q15 = 162
ARM_REG_Q0_Q1_Q2_Q3 = 163
ARM_REG_Q1_Q2_Q3_Q4 = 164
ARM_REG_Q2_Q3_Q4_Q5 = 165
ARM_REG_Q3_Q4_Q5_Q6 = 166
ARM_REG_Q4_Q5_Q6_Q7 = 167
ARM_REG_Q5_Q6_Q7_Q8 = 168
ARM_REG_Q6_Q7_Q8_Q9 = 169
ARM_REG_Q7_Q8_Q9_Q10 = 170
ARM_REG_Q8_Q9_Q10_Q11 = 171
ARM_REG_Q9_Q10_Q11_Q12 = 172
ARM_REG_Q10_Q11_Q12_Q13 = 173
ARM_REG_Q11_Q12_Q13_Q14 = 174
ARM_REG_Q12_Q13_Q14_Q15 = 175
ARM_REG_R0_R1 = 176
ARM_REG_R2_R3 = 177
ARM_REG_R4_R5 = 178
ARM_REG_R6_R7 = 179
ARM_REG_R8_R9 = 180
ARM_REG_R10_R11 = 181
ARM_REG_R12_SP = 182
ARM_REG_D0_D1_D2 = 183
ARM_REG_D1_D2_D3 = 184
ARM_REG_D2_D3_D4 = 185
ARM_REG_D3_D4_D5 = 186
ARM_REG_D4_D5_D6 = 187
ARM_REG_D5_D6_D7 = 188
ARM_REG_D6_D7_D8 = 189
ARM_REG_D7_D8_D9 = 190
ARM_REG_D8_D9_D10 = 191
ARM_REG_D9_D10_D11 = 192
ARM_REG_D10_D11_D12 = 193
ARM_REG_D11_D12_D13 = 194
ARM_REG_D12_D13_D14 = 195
ARM_REG_D13_D14_D15 = 196
ARM_REG_D14_D15_D16 = 197
ARM_REG_D15_D16_D17 = 198
ARM_REG_D16_D17_D18 = 199
ARM_REG_D17_D18_D19 = 200
ARM_REG_D18_D19_D20 = 201
ARM_REG_D19_D20_D21 = 202
ARM_REG_D20_D21_D22 = 203
ARM_REG_D21_D22_D23 = 204
ARM_REG_D22_D23_D24 = 205
ARM_REG_D23_D24_D25 = 206
ARM_REG_D24_D25_D26 = 207
ARM_REG_D25_D26_D27 = 208
ARM_REG_D26_D27_D28 = 209
ARM_REG_D27_D28_D29 = 210
ARM_REG_D28_D29_D30 = 211
ARM_REG_D29_D30_D31 = 212
ARM_REG_D0_D2_D4 = 213
ARM_REG_D1_D3_D5 = 214
ARM_REG_D2_D4_D6 = 215
ARM_REG_D3_D5_D7 = 216
ARM_REG_D4_D6_D8 = 217
ARM_REG_D5_D7_D9 = 218
ARM_REG_D6_D8_D10 = 219
ARM_REG_D7_D9_D11 = 220
ARM_REG_D8_D10_D12 = 221
ARM_REG_D9_D11_D13 = 222
ARM_REG_D10_D12_D14 = 223
ARM_REG_D11_D13_D15 = 224
ARM_REG_D12_D14_D16 = 225
ARM_REG_D13_D15_D17 = 226
ARM_REG_D14_D16_D18 = 227
ARM_REG_D15_D17_D19 = 228
ARM_REG_D16_D18_D20 = 229
ARM_REG_D17_D19_D21 = 230
ARM_REG_D18_D20_D22 = 231
ARM_REG_D19_D21_D23 = 232
ARM_REG_D20_D22_D24 = 233
ARM_REG_D21_D23_D25 = 234
ARM_REG_D22_D24_D26 = 235
ARM_REG_D23_D25_D27 = 236
ARM_REG_D24_D26_D28 = 237
ARM_REG_D25_D27_D29 = 238
ARM_REG_D26_D28_D30 = 239
ARM_REG_D27_D29_D31 = 240
ARM_REG_D0_D2_D4_D6 = 241
ARM_REG_D1_D3_D5_D7 = 242
ARM_REG_D2_D4_D6_D8 = 243
ARM_REG_D3_D5_D7_D9 = 244
ARM_REG_D4_D6_D8_D10 = 245
ARM_REG_D5_D7_D9_D11 = 246
ARM_REG_D6_D8_D10_D12 = 247
ARM_REG_D7_D9_D11_D13 = 248
ARM_REG_D8_D10_D12_D14 = 249
ARM_REG_D9_D11_D13_D15 = 250
ARM_REG_D10_D12_D14_D16 = 251
ARM_REG_D11_D13_D15_D17 = 252
ARM_REG_D12_D14_D16_D18 = 253
ARM_REG_D13_D15_D17_D19 = 254
ARM_REG_D14_D16_D18_D20 = 255
ARM_REG_D15_D17_D19_D21 = 256
ARM_REG_D16_D18_D20_D22 = 257
ARM_REG_D17_D19_D21_D23 = 258
ARM_REG_D18_D20_D22_D24 = 259
ARM_REG_D19_D21_D23_D25 = 260
ARM_REG_D20_D22_D24_D26 = 261
ARM_REG_D21_D23_D25_D27 = 262
ARM_REG_D22_D24_D26_D28 = 263
ARM_REG_D23_D25_D27_D29 = 264
ARM_REG_D24_D26_D28_D30 = 265
ARM_REG_D25_D27_D29_D31 = 266
ARM_REG_D1_D2 = 267
ARM_REG_D3_D4 = 268
ARM_REG_D5_D6 = 269
ARM_REG_D7_D8 = 270
ARM_REG_D9_D10 = 271
ARM_REG_D11_D12 = 272
ARM_REG_D13_D14 = 273
ARM_REG_D15_D16 = 274
ARM_REG_D17_D18 = 275
ARM_REG_D19_D20 = 276
ARM_REG_D21_D22 = 277
ARM_REG_D23_D24 = 278
ARM_REG_D25_D26 = 279
ARM_REG_D27_D28 = 280
ARM_REG_D29_D30 = 281
ARM_REG_D1_D2_D3_D4 = 282
ARM_REG_D3_D4_D5_D6 = 283
ARM_REG_D5_D6_D7_D8 = 284
ARM_REG_D7_D8_D9_D10 = 285
ARM_REG_D9_D10_D11_D12 = 286
ARM_REG_D11_D12_D13_D14 = 287
ARM_REG_D13_D14_D15_D16 = 288
ARM_REG_D15_D16_D17_D18 = 289
ARM_REG_D17_D18_D19_D20 = 290
ARM_REG_D19_D20_D21_D22 = 291
ARM_REG_D21_D22_D23_D24 = 292
ARM_REG_D23_D24_D25_D26 = 293
ARM_REG_D25_D26_D27_D28 = 294
ARM_REG_D27_D28_D29_D30 = 295
ARM_REG_ENDING = 296
ARM_REG_R13 = ARM_REG_SP
ARM_REG_R14 = ARM_REG_LR
ARM_REG_R15 = ARM_REG_PC
ARM_REG_SB = ARM_REG_R9
ARM_REG_SL = ARM_REG_R10
ARM_REG_FP = ARM_REG_R11
ARM_REG_IP = ARM_REG_R12

ARM_INS_INVALID = 0
ARM_INS_ASR = 1
ARM_INS_IT = 2
ARM_INS_LDRBT = 3
ARM_INS_LDR = 4
ARM_INS_LDRHT = 5
ARM_INS_LDRSBT = 6
ARM_INS_LDRSHT = 7
ARM_INS_LDRT = 8
ARM_INS_LSL = 9
ARM_INS_LSR = 10
ARM_INS_ROR = 11
ARM_INS_RRX = 12
ARM_INS_STRBT = 13
ARM_INS_STRT = 14
ARM_INS_VLD1 = 15
ARM_INS_VLD2 = 16
ARM_INS_VLD3 = 17
ARM_INS_VLD4 = 18
ARM_INS_VST1 = 19
ARM_INS_VST2 = 20
ARM_INS_VST3 = 21
ARM_INS_VST4 = 22
ARM_INS_LDRB = 23
ARM_INS_LDRH = 24
ARM_INS_LDRSB = 25
ARM_INS_LDRSH = 26
ARM_INS_MOVS = 27
ARM_INS_MOV = 28
ARM_INS_STR = 29
ARM_INS_ADC = 30
ARM_INS_ADD = 31
ARM_INS_ADR = 32
ARM_INS_AESD = 33
ARM_INS_AESE = 34
ARM_INS_AESIMC = 35
ARM_INS_AESMC = 36
ARM_INS_AND = 37
ARM_INS_VDOT = 38
ARM_INS_VCVT = 39
ARM_INS_VCVTB = 40
ARM_INS_VCVTT = 41
ARM_INS_BFC = 42
ARM_INS_BFI = 43
ARM_INS_BIC = 44
ARM_INS_BKPT = 45
ARM_INS_BL = 46
ARM_INS_BLX = 47
ARM_INS_BX = 48
ARM_INS_BXJ = 49
ARM_INS_B = 50
ARM_INS_CX1 = 51
ARM_INS_CX1A = 52
ARM_INS_CX1D = 53
ARM_INS_CX1DA = 54
ARM_INS_CX2 = 55
ARM_INS_CX2A = 56
ARM_INS_CX2D = 57
ARM_INS_CX2DA = 58
ARM_INS_CX3 = 59
ARM_INS_CX3A = 60
ARM_INS_CX3D = 61
ARM_INS_CX3DA = 62
ARM_INS_VCX1A = 63
ARM_INS_VCX1 = 64
ARM_INS_VCX2A = 65
ARM_INS_VCX2 = 66
ARM_INS_VCX3A = 67
ARM_INS_VCX3 = 68
ARM_INS_CDP = 69
ARM_INS_CDP2 = 70
ARM_INS_CLREX = 71
ARM_INS_CLZ = 72
ARM_INS_CMN = 73
ARM_INS_CMP = 74
ARM_INS_CPS = 75
ARM_INS_CRC32B = 76
ARM_INS_CRC32CB = 77
ARM_INS_CRC32CH = 78
ARM_INS_CRC32CW = 79
ARM_INS_CRC32H = 80
ARM_INS_CRC32W = 81
ARM_INS_DBG = 82
ARM_INS_DMB = 83
ARM_INS_DSB = 84
ARM_INS_EOR = 85
ARM_INS_ERET = 86
ARM_INS_VMOV = 87
ARM_INS_FLDMDBX = 88
ARM_INS_FLDMIAX = 89
ARM_INS_VMRS = 90
ARM_INS_FSTMDBX = 91
ARM_INS_FSTMIAX = 92
ARM_INS_HINT = 93
ARM_INS_HLT = 94
ARM_INS_HVC = 95
ARM_INS_ISB = 96
ARM_INS_LDA = 97
ARM_INS_LDAB = 98
ARM_INS_LDAEX = 99
ARM_INS_LDAEXB = 100
ARM_INS_LDAEXD = 101
ARM_INS_LDAEXH = 102
ARM_INS_LDAH = 103
ARM_INS_LDC2L = 104
ARM_INS_LDC2 = 105
ARM_INS_LDCL = 106
ARM_INS_LDC = 107
ARM_INS_LDMDA = 108
ARM_INS_LDMDB = 109
ARM_INS_LDM = 110
ARM_INS_LDMIB = 111
ARM_INS_LDRD = 112
ARM_INS_LDREX = 113
ARM_INS_LDREXB = 114
ARM_INS_LDREXD = 115
ARM_INS_LDREXH = 116
ARM_INS_MCR = 117
ARM_INS_MCR2 = 118
ARM_INS_MCRR = 119
ARM_INS_MCRR2 = 120
ARM_INS_MLA = 121
ARM_INS_MLS = 122
ARM_INS_MOVT = 123
ARM_INS_MOVW = 124
ARM_INS_MRC = 125
ARM_INS_MRC2 = 126
ARM_INS_MRRC = 127
ARM_INS_MRRC2 = 128
ARM_INS_MRS = 129
ARM_INS_MSR = 130
ARM_INS_MUL = 131
ARM_INS_ASRL = 132
ARM_INS_DLSTP = 133
ARM_INS_LCTP = 134
ARM_INS_LETP = 135
ARM_INS_LSLL = 136
ARM_INS_LSRL = 137
ARM_INS_SQRSHR = 138
ARM_INS_SQRSHRL = 139
ARM_INS_SQSHL = 140
ARM_INS_SQSHLL = 141
ARM_INS_SRSHR = 142
ARM_INS_SRSHRL = 143
ARM_INS_UQRSHL = 144
ARM_INS_UQRSHLL = 145
ARM_INS_UQSHL = 146
ARM_INS_UQSHLL = 147
ARM_INS_URSHR = 148
ARM_INS_URSHRL = 149
ARM_INS_VABAV = 150
ARM_INS_VABD = 151
ARM_INS_VABS = 152
ARM_INS_VADC = 153
ARM_INS_VADCI = 154
ARM_INS_VADDLVA = 155
ARM_INS_VADDLV = 156
ARM_INS_VADDVA = 157
ARM_INS_VADDV = 158
ARM_INS_VADD = 159
ARM_INS_VAND = 160
ARM_INS_VBIC = 161
ARM_INS_VBRSR = 162
ARM_INS_VCADD = 163
ARM_INS_VCLS = 164
ARM_INS_VCLZ = 165
ARM_INS_VCMLA = 166
ARM_INS_VCMP = 167
ARM_INS_VCMUL = 168
ARM_INS_VCTP = 169
ARM_INS_VCVTA = 170
ARM_INS_VCVTM = 171
ARM_INS_VCVTN = 172
ARM_INS_VCVTP = 173
ARM_INS_VDDUP = 174
ARM_INS_VDUP = 175
ARM_INS_VDWDUP = 176
ARM_INS_VEOR = 177
ARM_INS_VFMAS = 178
ARM_INS_VFMA = 179
ARM_INS_VFMS = 180
ARM_INS_VHADD = 181
ARM_INS_VHCADD = 182
ARM_INS_VHSUB = 183
ARM_INS_VIDUP = 184
ARM_INS_VIWDUP = 185
ARM_INS_VLD20 = 186
ARM_INS_VLD21 = 187
ARM_INS_VLD40 = 188
ARM_INS_VLD41 = 189
ARM_INS_VLD42 = 190
ARM_INS_VLD43 = 191
ARM_INS_VLDRB = 192
ARM_INS_VLDRD = 193
ARM_INS_VLDRH = 194
ARM_INS_VLDRW = 195
ARM_INS_VMAXAV = 196
ARM_INS_VMAXA = 197
ARM_INS_VMAXNMAV = 198
ARM_INS_VMAXNMA = 199
ARM_INS_VMAXNMV = 200
ARM_INS_VMAXNM = 201
ARM_INS_VMAXV = 202
ARM_INS_VMAX = 203
ARM_INS_VMINAV = 204
ARM_INS_VMINA = 205
ARM_INS_VMINNMAV = 206
ARM_INS_VMINNMA = 207
ARM_INS_VMINNMV = 208
ARM_INS_VMINNM = 209
ARM_INS_VMINV = 210
ARM_INS_VMIN = 211
ARM_INS_VMLADAVA = 212
ARM_INS_VMLADAVAX = 213
ARM_INS_VMLADAV = 214
ARM_INS_VMLADAVX = 215
ARM_INS_VMLALDAVA = 216
ARM_INS_VMLALDAVAX = 217
ARM_INS_VMLALDAV = 218
ARM_INS_VMLALDAVX = 219
ARM_INS_VMLAS = 220
ARM_INS_VMLA = 221
ARM_INS_VMLSDAVA = 222
ARM_INS_VMLSDAVAX = 223
ARM_INS_VMLSDAV = 224
ARM_INS_VMLSDAVX = 225
ARM_INS_VMLSLDAVA = 226
ARM_INS_VMLSLDAVAX = 227
ARM_INS_VMLSLDAV = 228
ARM_INS_VMLSLDAVX = 229
ARM_INS_VMOVLB = 230
ARM_INS_VMOVLT = 231
ARM_INS_VMOVNB = 232
ARM_INS_VMOVNT = 233
ARM_INS_VMULH = 234
ARM_INS_VMULLB = 235
ARM_INS_VMULLT = 236
ARM_INS_VMUL = 237
ARM_INS_VMVN = 238
ARM_INS_VNEG = 239
ARM_INS_VORN = 240
ARM_INS_VORR = 241
ARM_INS_VPNOT = 242
ARM_INS_VPSEL = 243
ARM_INS_VPST = 244
ARM_INS_VPT = 245
ARM_INS_VQABS = 246
ARM_INS_VQADD = 247
ARM_INS_VQDMLADHX = 248
ARM_INS_VQDMLADH = 249
ARM_INS_VQDMLAH = 250
ARM_INS_VQDMLASH = 251
ARM_INS_VQDMLSDHX = 252
ARM_INS_VQDMLSDH = 253
ARM_INS_VQDMULH = 254
ARM_INS_VQDMULLB = 255
ARM_INS_VQDMULLT = 256
ARM_INS_VQMOVNB = 257
ARM_INS_VQMOVNT = 258
ARM_INS_VQMOVUNB = 259
ARM_INS_VQMOVUNT = 260
ARM_INS_VQNEG = 261
ARM_INS_VQRDMLADHX = 262
ARM_INS_VQRDMLADH = 263
ARM_INS_VQRDMLAH = 264
ARM_INS_VQRDMLASH = 265
ARM_INS_VQRDMLSDHX = 266
ARM_INS_VQRDMLSDH = 267
ARM_INS_VQRDMULH = 268
ARM_INS_VQRSHL = 269
ARM_INS_VQRSHRNB = 270
ARM_INS_VQRSHRNT = 271
ARM_INS_VQRSHRUNB = 272
ARM_INS_VQRSHRUNT = 273
ARM_INS_VQSHLU = 274
ARM_INS_VQSHL = 275
ARM_INS_VQSHRNB = 276
ARM_INS_VQSHRNT = 277
ARM_INS_VQSHRUNB = 278
ARM_INS_VQSHRUNT = 279
ARM_INS_VQSUB = 280
ARM_INS_VREV16 = 281
ARM_INS_VREV32 = 282
ARM_INS_VREV64 = 283
ARM_INS_VRHADD = 284
ARM_INS_VRINTA = 285
ARM_INS_VRINTM = 286
ARM_INS_VRINTN = 287
ARM_INS_VRINTP = 288
ARM_INS_VRINTX = 289
ARM_INS_VRINTZ = 290
ARM_INS_VRMLALDAVHA = 291
ARM_INS_VRMLALDAVHAX = 292
ARM_INS_VRMLALDAVH = 293
ARM_INS_VRMLALDAVHX = 294
ARM_INS_VRMLSLDAVHA = 295
ARM_INS_VRMLSLDAVHAX = 296
ARM_INS_VRMLSLDAVH = 297
ARM_INS_VRMLSLDAVHX = 298
ARM_INS_VRMULH = 299
ARM_INS_VRSHL = 300
ARM_INS_VRSHRNB = 301
ARM_INS_VRSHRNT = 302
ARM_INS_VRSHR = 303
ARM_INS_VSBC = 304
ARM_INS_VSBCI = 305
ARM_INS_VSHLC = 306
ARM_INS_VSHLLB = 307
ARM_INS_VSHLLT = 308
ARM_INS_VSHL = 309
ARM_INS_VSHRNB = 310
ARM_INS_VSHRNT = 311
ARM_INS_VSHR = 312
ARM_INS_VSLI = 313
ARM_INS_VSRI = 314
ARM_INS_VST20 = 315
ARM_INS_VST21 = 316
ARM_INS_VST40 = 317
ARM_INS_VST41 = 318
ARM_INS_VST42 = 319
ARM_INS_VST43 = 320
ARM_INS_VSTRB = 321
ARM_INS_VSTRD = 322
ARM_INS_VSTRH = 323
ARM_INS_VSTRW = 324
ARM_INS_VSUB = 325
ARM_INS_WLSTP = 326
ARM_INS_MVN = 327
ARM_INS_ORR = 328
ARM_INS_PKHBT = 329
ARM_INS_PKHTB = 330
ARM_INS_PLDW = 331
ARM_INS_PLD = 332
ARM_INS_PLI = 333
ARM_INS_QADD = 334
ARM_INS_QADD16 = 335
ARM_INS_QADD8 = 336
ARM_INS_QASX = 337
ARM_INS_QDADD = 338
ARM_INS_QDSUB = 339
ARM_INS_QSAX = 340
ARM_INS_QSUB = 341
ARM_INS_QSUB16 = 342
ARM_INS_QSUB8 = 343
ARM_INS_RBIT = 344
ARM_INS_REV = 345
ARM_INS_REV16 = 346
ARM_INS_REVSH = 347
ARM_INS_RFEDA = 348
ARM_INS_RFEDB = 349
ARM_INS_RFEIA = 350
ARM_INS_RFEIB = 351
ARM_INS_RSB = 352
ARM_INS_RSC = 353
ARM_INS_SADD16 = 354
ARM_INS_SADD8 = 355
ARM_INS_SASX = 356
ARM_INS_SB = 357
ARM_INS_SBC = 358
ARM_INS_SBFX = 359
ARM_INS_SDIV = 360
ARM_INS_SEL = 361
ARM_INS_SETEND = 362
ARM_INS_SETPAN = 363
ARM_INS_SHA1C = 364
ARM_INS_SHA1H = 365
ARM_INS_SHA1M = 366
ARM_INS_SHA1P = 367
ARM_INS_SHA1SU0 = 368
ARM_INS_SHA1SU1 = 369
ARM_INS_SHA256H = 370
ARM_INS_SHA256H2 = 371
ARM_INS_SHA256SU0 = 372
ARM_INS_SHA256SU1 = 373
ARM_INS_SHADD16 = 374
ARM_INS_SHADD8 = 375
ARM_INS_SHASX = 376
ARM_INS_SHSAX = 377
ARM_INS_SHSUB16 = 378
ARM_INS_SHSUB8 = 379
ARM_INS_SMC = 380
ARM_INS_SMLABB = 381
ARM_INS_SMLABT = 382
ARM_INS_SMLAD = 383
ARM_INS_SMLADX = 384
ARM_INS_SMLAL = 385
ARM_INS_SMLALBB = 386
ARM_INS_SMLALBT = 387
ARM_INS_SMLALD = 388
ARM_INS_SMLALDX = 389
ARM_INS_SMLALTB = 390
ARM_INS_SMLALTT = 391
ARM_INS_SMLATB = 392
ARM_INS_SMLATT = 393
ARM_INS_SMLAWB = 394
ARM_INS_SMLAWT = 395
ARM_INS_SMLSD = 396
ARM_INS_SMLSDX = 397
ARM_INS_SMLSLD = 398
ARM_INS_SMLSLDX = 399
ARM_INS_SMMLA = 400
ARM_INS_SMMLAR = 401
ARM_INS_SMMLS = 402
ARM_INS_SMMLSR = 403
ARM_INS_SMMUL = 404
ARM_INS_SMMULR = 405
ARM_INS_SMUAD = 406
ARM_INS_SMUADX = 407
ARM_INS_SMULBB = 408
ARM_INS_SMULBT = 409
ARM_INS_SMULL = 410
ARM_INS_SMULTB = 411
ARM_INS_SMULTT = 412
ARM_INS_SMULWB = 413
ARM_INS_SMULWT = 414
ARM_INS_SMUSD = 415
ARM_INS_SMUSDX = 416
ARM_INS_SRSDA = 417
ARM_INS_SRSDB = 418
ARM_INS_SRSIA = 419
ARM_INS_SRSIB = 420
ARM_INS_SSAT = 421
ARM_INS_SSAT16 = 422
ARM_INS_SSAX = 423
ARM_INS_SSUB16 = 424
ARM_INS_SSUB8 = 425
ARM_INS_STC2L = 426
ARM_INS_STC2 = 427
ARM_INS_STCL = 428
ARM_INS_STC = 429
ARM_INS_STL = 430
ARM_INS_STLB = 431
ARM_INS_STLEX = 432
ARM_INS_STLEXB = 433
ARM_INS_STLEXD = 434
ARM_INS_STLEXH = 435
ARM_INS_STLH = 436
ARM_INS_STMDA = 437
ARM_INS_STMDB = 438
ARM_INS_STM = 439
ARM_INS_STMIB = 440
ARM_INS_STRB = 441
ARM_INS_STRD = 442
ARM_INS_STREX = 443
ARM_INS_STREXB = 444
ARM_INS_STREXD = 445
ARM_INS_STREXH = 446
ARM_INS_STRH = 447
ARM_INS_STRHT = 448
ARM_INS_SUB = 449
ARM_INS_SVC = 450
ARM_INS_SWP = 451
ARM_INS_SWPB = 452
ARM_INS_SXTAB = 453
ARM_INS_SXTAB16 = 454
ARM_INS_SXTAH = 455
ARM_INS_SXTB = 456
ARM_INS_SXTB16 = 457
ARM_INS_SXTH = 458
ARM_INS_TEQ = 459
ARM_INS_TRAP = 460
ARM_INS_TSB = 461
ARM_INS_TST = 462
ARM_INS_UADD16 = 463
ARM_INS_UADD8 = 464
ARM_INS_UASX = 465
ARM_INS_UBFX = 466
ARM_INS_UDF = 467
ARM_INS_UDIV = 468
ARM_INS_UHADD16 = 469
ARM_INS_UHADD8 = 470
ARM_INS_UHASX = 471
ARM_INS_UHSAX = 472
ARM_INS_UHSUB16 = 473
ARM_INS_UHSUB8 = 474
ARM_INS_UMAAL = 475
ARM_INS_UMLAL = 476
ARM_INS_UMULL = 477
ARM_INS_UQADD16 = 478
ARM_INS_UQADD8 = 479
ARM_INS_UQASX = 480
ARM_INS_UQSAX = 481
ARM_INS_UQSUB16 = 482
ARM_INS_UQSUB8 = 483
ARM_INS_USAD8 = 484
ARM_INS_USADA8 = 485
ARM_INS_USAT = 486
ARM_INS_USAT16 = 487
ARM_INS_USAX = 488
ARM_INS_USUB16 = 489
ARM_INS_USUB8 = 490
ARM_INS_UXTAB = 491
ARM_INS_UXTAB16 = 492
ARM_INS_UXTAH = 493
ARM_INS_UXTB = 494
ARM_INS_UXTB16 = 495
ARM_INS_UXTH = 496
ARM_INS_VABAL = 497
ARM_INS_VABA = 498
ARM_INS_VABDL = 499
ARM_INS_VACGE = 500
ARM_INS_VACGT = 501
ARM_INS_VADDHN = 502
ARM_INS_VADDL = 503
ARM_INS_VADDW = 504
ARM_INS_VFMAB = 505
ARM_INS_VFMAT = 506
ARM_INS_VBIF = 507
ARM_INS_VBIT = 508
ARM_INS_VBSL = 509
ARM_INS_VCEQ = 510
ARM_INS_VCGE = 511
ARM_INS_VCGT = 512
ARM_INS_VCLE = 513
ARM_INS_VCLT = 514
ARM_INS_VCMPE = 515
ARM_INS_VCNT = 516
ARM_INS_VDIV = 517
ARM_INS_VEXT = 518
ARM_INS_VFMAL = 519
ARM_INS_VFMSL = 520
ARM_INS_VFNMA = 521
ARM_INS_VFNMS = 522
ARM_INS_VINS = 523
ARM_INS_VJCVT = 524
ARM_INS_VLDMDB = 525
ARM_INS_VLDMIA = 526
ARM_INS_VLDR = 527
ARM_INS_VLLDM = 528
ARM_INS_VLSTM = 529
ARM_INS_VMLAL = 530
ARM_INS_VMLS = 531
ARM_INS_VMLSL = 532
ARM_INS_VMMLA = 533
ARM_INS_VMOVX = 534
ARM_INS_VMOVL = 535
ARM_INS_VMOVN = 536
ARM_INS_VMSR = 537
ARM_INS_VMULL = 538
ARM_INS_VNMLA = 539
ARM_INS_VNMLS = 540
ARM_INS_VNMUL = 541
ARM_INS_VPADAL = 542
ARM_INS_VPADDL = 543
ARM_INS_VPADD = 544
ARM_INS_VPMAX = 545
ARM_INS_VPMIN = 546
ARM_INS_VQDMLAL = 547
ARM_INS_VQDMLSL = 548
ARM_INS_VQDMULL = 549
ARM_INS_VQMOVUN = 550
ARM_INS_VQMOVN = 551
ARM_INS_VQRDMLSH = 552
ARM_INS_VQRSHRN = 553
ARM_INS_VQRSHRUN = 554
ARM_INS_VQSHRN = 555
ARM_INS_VQSHRUN = 556
ARM_INS_VRADDHN = 557
ARM_INS_VRECPE = 558
ARM_INS_VRECPS = 559
ARM_INS_VRINTR = 560
ARM_INS_VRSHRN = 561
ARM_INS_VRSQRTE = 562
ARM_INS_VRSQRTS = 563
ARM_INS_VRSRA = 564
ARM_INS_VRSUBHN = 565
ARM_INS_VSCCLRM = 566
ARM_INS_VSDOT = 567
ARM_INS_VSELEQ = 568
ARM_INS_VSELGE = 569
ARM_INS_VSELGT = 570
ARM_INS_VSELVS = 571
ARM_INS_VSHLL = 572
ARM_INS_VSHRN = 573
ARM_INS_VSMMLA = 574
ARM_INS_VSQRT = 575
ARM_INS_VSRA = 576
ARM_INS_VSTMDB = 577
ARM_INS_VSTMIA = 578
ARM_INS_VSTR = 579
ARM_INS_VSUBHN = 580
ARM_INS_VSUBL = 581
ARM_INS_VSUBW = 582
ARM_INS_VSUDOT = 583
ARM_INS_VSWP = 584
ARM_INS_VTBL = 585
ARM_INS_VTBX = 586
ARM_INS_VCVTR = 587
ARM_INS_VTRN = 588
ARM_INS_VTST = 589
ARM_INS_VUDOT = 590
ARM_INS_VUMMLA = 591
ARM_INS_VUSDOT = 592
ARM_INS_VUSMMLA = 593
ARM_INS_VUZP = 594
ARM_INS_VZIP = 595
ARM_INS_ADDW = 596
ARM_INS_AUT = 597
ARM_INS_AUTG = 598
ARM_INS_BFL = 599
ARM_INS_BFLX = 600
ARM_INS_BF = 601
ARM_INS_BFCSEL = 602
ARM_INS_BFX = 603
ARM_INS_BTI = 604
ARM_INS_BXAUT = 605
ARM_INS_CLRM = 606
ARM_INS_CSEL = 607
ARM_INS_CSINC = 608
ARM_INS_CSINV = 609
ARM_INS_CSNEG = 610
ARM_INS_DCPS1 = 611
ARM_INS_DCPS2 = 612
ARM_INS_DCPS3 = 613
ARM_INS_DLS = 614
ARM_INS_LE = 615
ARM_INS_ORN = 616
ARM_INS_PAC = 617
ARM_INS_PACBTI = 618
ARM_INS_PACG = 619
ARM_INS_SG = 620
ARM_INS_SUBS = 621
ARM_INS_SUBW = 622
ARM_INS_TBB = 623
ARM_INS_TBH = 624
ARM_INS_TT = 625
ARM_INS_TTA = 626
ARM_INS_TTAT = 627
ARM_INS_TTT = 628
ARM_INS_WLS = 629
ARM_INS_BLXNS = 630
ARM_INS_BXNS = 631
ARM_INS_CBNZ = 632
ARM_INS_CBZ = 633
ARM_INS_POP = 634
ARM_INS_PUSH = 635
ARM_INS___BRKDIV0 = 636
ARM_INS_ENDING = 637
ARM_INS_ALIAS_BEGIN = 638
ARM_INS_ALIAS_VMOV = 639
ARM_INS_ALIAS_NOP = 640
ARM_INS_ALIAS_YIELD = 641
ARM_INS_ALIAS_WFE = 642
ARM_INS_ALIAS_WFI = 643
ARM_INS_ALIAS_SEV = 644
ARM_INS_ALIAS_SEVL = 645
ARM_INS_ALIAS_ESB = 646
ARM_INS_ALIAS_CSDB = 647
ARM_INS_ALIAS_CLRBHB = 648
ARM_INS_ALIAS_PACBTI = 649
ARM_INS_ALIAS_BTI = 650
ARM_INS_ALIAS_PAC = 651
ARM_INS_ALIAS_AUT = 652
ARM_INS_ALIAS_SSBB = 653
ARM_INS_ALIAS_PSSBB = 654
ARM_INS_ALIAS_DFB = 655
ARM_INS_ALIAS_CSETM = 656
ARM_INS_ALIAS_CSET = 657
ARM_INS_ALIAS_CINC = 658
ARM_INS_ALIAS_CINV = 659
ARM_INS_ALIAS_CNEG = 660
ARM_INS_ALIAS_VMLAV = 661
ARM_INS_ALIAS_VMLAVA = 662
ARM_INS_ALIAS_VRMLALVH = 663
ARM_INS_ALIAS_VRMLALVHA = 664
ARM_INS_ALIAS_VMLALV = 665
ARM_INS_ALIAS_VMLALVA = 666
ARM_INS_ALIAS_VBIC = 667
ARM_INS_ALIAS_VEOR = 668
ARM_INS_ALIAS_VORN = 669
ARM_INS_ALIAS_VORR = 670
ARM_INS_ALIAS_VAND = 671
ARM_INS_ALIAS_VPSEL = 672
ARM_INS_ALIAS_ERET = 673
ARM_INS_ALIAS_ASR = 674
ARM_INS_ALIAS_LSL = 675
ARM_INS_ALIAS_LSR = 676
ARM_INS_ALIAS_ROR = 677
ARM_INS_ALIAS_RRX = 678
ARM_INS_ALIAS_UXTW = 679
ARM_INS_ALIAS_LDM = 680
ARM_INS_ALIAS_POP = 681
ARM_INS_ALIAS_PUSH = 682
ARM_INS_ALIAS_POPW = 683
ARM_INS_ALIAS_PUSHW = 684
ARM_INS_ALIAS_VPOP = 685
ARM_INS_ALIAS_VPUSH = 686
ARM_INS_ALIAS_END = 687

ARM_GRP_INVALID = 0
ARM_GRP_JUMP = 1
ARM_GRP_CALL = 2
ARM_GRP_RET = 3
ARM_GRP_INT = 4
ARM_GRP_PRIVILEGE = 6
ARM_GRP_BRANCH_RELATIVE = 7
ARM_FEATURE_IsARM = 128
ARM_FEATURE_HasV5T = 129
ARM_FEATURE_HasV4T = 130
ARM_FEATURE_HasVFP2 = 131
ARM_FEATURE_HasV5TE = 132
ARM_FEATURE_HasV6T2 = 133
ARM_FEATURE_HasMVEInt = 134
ARM_FEATURE_HasNEON = 135
ARM_FEATURE_HasFPRegs64 = 136
ARM_FEATURE_HasFPRegs = 137
ARM_FEATURE_IsThumb2 = 138
ARM_FEATURE_HasV8_1MMainline = 139
ARM_FEATURE_HasLOB = 140
ARM_FEATURE_IsThumb = 141
ARM_FEATURE_HasV8MBaseline = 142
ARM_FEATURE_Has8MSecExt = 143
ARM_FEATURE_HasV8 = 144
ARM_FEATURE_HasAES = 145
ARM_FEATURE_HasBF16 = 146
ARM_FEATURE_HasCDE = 147
ARM_FEATURE_PreV8 = 148
ARM_FEATURE_HasV6K = 149
ARM_FEATURE_HasCRC = 150
ARM_FEATURE_HasV7 = 151
ARM_FEATURE_HasDB = 152
ARM_FEATURE_HasVirtualization = 153
ARM_FEATURE_HasVFP3 = 154
ARM_FEATURE_HasDPVFP = 155
ARM_FEATURE_HasFullFP16 = 156
ARM_FEATURE_HasV6 = 157
ARM_FEATURE_HasAcquireRelease = 158
ARM_FEATURE_HasV7Clrex = 159
ARM_FEATURE_HasMVEFloat = 160
ARM_FEATURE_HasFPRegsV8_1M = 161
ARM_FEATURE_HasMP = 162
ARM_FEATURE_HasSB = 163
ARM_FEATURE_HasDivideInARM = 164
ARM_FEATURE_HasV8_1a = 165
ARM_FEATURE_HasSHA2 = 166
ARM_FEATURE_HasTrustZone = 167
ARM_FEATURE_UseNaClTrap = 168
ARM_FEATURE_HasV8_4a = 169
ARM_FEATURE_HasV8_3a = 170
ARM_FEATURE_HasFPARMv8 = 171
ARM_FEATURE_HasFP16 = 172
ARM_FEATURE_HasVFP4 = 173
ARM_FEATURE_HasFP16FML = 174
ARM_FEATURE_HasFPRegs16 = 175
ARM_FEATURE_HasV8MMainline = 176
ARM_FEATURE_HasDotProd = 177
ARM_FEATURE_HasMatMulInt8 = 178
ARM_FEATURE_IsMClass = 179
ARM_FEATURE_HasPACBTI = 180
ARM_FEATURE_IsNotMClass = 181
ARM_FEATURE_HasDSP = 182
ARM_FEATURE_HasDivideInThumb = 183
ARM_FEATURE_HasV6M = 184
ARM_GRP_ENDING = 185
