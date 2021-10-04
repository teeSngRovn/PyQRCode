import CorrectionCode

M = 10
Bit ={
    -1:0, 0:1
}
prefix =[1, 1, 1, 0, 1] #PATTERN 5
#PATTERN 101
XOR = [1,0,1,0,1,0,0,0,0,0,1,0,0,1,0]


MessageCode = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, -1, 0, 0, 0]
PatternCode = MessageCode[:]
N = len(PatternCode) - 1
GeneratorPolynomial = [0, 0, 0, -1, 0, 0, -1, -1, 0, -1, 0]
for i in range(len(MessageCode)-M):
    if -1 != PatternCode[N]:
        K = PatternCode[N]
        for j in range(N - M, N+1):
            if PatternCode[j] != -1:
                A = CorrectionCode.Alpha.alpha[PatternCode[j]]
            else:
                A = 0
            if GeneratorPolynomial[j - (N-M)] != -1:
                B = CorrectionCode.Alpha.alpha[(K + GeneratorPolynomial[j - (N-10)]) % 255]
            else:
                B = 0
            PatternCode[j] = CorrectionCode.Alpha.map[A ^ B]
    N = N - 1

FormatBit = []
for i in range(M):
    FormatBit.append(Bit[PatternCode[i]])
FormatBit.reverse()
FormatBit = prefix + FormatBit

FormatBits = ''
for i in range(len(FormatBit)):
    FormatBit[i] = FormatBit[i] ^ XOR[i]
    FormatBits = FormatBits + str(FormatBit[i])
print(FormatBits)