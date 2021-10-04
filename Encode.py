import CorrectionCode


M = 22
databit = 176

Code = {
    '0':0, '1':1, '2':2, '3':3, '4':4, '5':5,
    '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11,
    'C':12, 'D':13, 'E':14, 'F':15, 'G':16, 'H':17,
    'I':18, 'J':19, 'K':20, 'L':21, 'M':22, 'N':23,
    'O':24, 'P':25, 'Q':26, 'R':27, 'S':28, 'T':29,
    'U':30, 'V':31, 'W':32, 'X':33, 'Y':34, 'Z':35,
    ' ':36, '$':37, '%':38, '*':39, '+':40, '-':41, 
    '.':42, '/':43, ':':44
}
Padding = {
    0:'11101100', 1:'00010001'
}
def Dec2Bin(Dec, Bits):
    Bin = ''
    while (Dec != 0):
        Bin = str(Dec % 2) + Bin
        Dec = Dec // 2
    if len(Bin)<Bits:
        Bin = '0'*(Bits - len(Bin)) + Bin
    return Bin
def Bin2Dec(Bin):
    Dec = 0
    for i in range(0, len(Bin)):
        Dec = Dec*2 + int(Bin[i])
    return Dec


def EncodedData(Data, NODB):
    Words = []
    for i in range(0, len(Data)):
        Words.append(Code[Data[i]])
    a = Words[0::2]
    b = Words[1::2]
    #change Opt to Bin 
    EncodedData = ''
    for i in range(0,len(a)):
        if (i == len(a)-1)and(len(b)<len(a)):
            EncodedData = EncodedData + Dec2Bin(a[i], 6)
        else:
            EncodedData = EncodedData + Dec2Bin(a[i]*45 + b[i], 11)

    EncodedData = '0010' + Dec2Bin(len(Data), 9) + EncodedData + '0'*4
    EncodedData = EncodedData + '0'*(8 - len(EncodedData) % 8)
    #add padding code to get NODB
    i = 0
    while len(EncodedData) < NODB:
        EncodedData = EncodedData + Padding[i]
        i = (i + 1) % 2
    #Make Codewords
    CodeWords = []
    for i in range(0, NODB, 8):
        CodeWords.append(Bin2Dec(EncodedData[i:i+8]))
    return CodeWords


def ENCOEDE(STRING):
    #Input Data
    Data = STRING
    CodeWords = EncodedData(Data, databit)
    MessageCodewords = CodeWords[:]
    CodeWords.reverse()

    for i in range(len(CodeWords)):
        CodeWords[i] = CorrectionCode.Alpha.map[CodeWords[i]]

    for i in range(M):
        CodeWords.append(-1)

    for i in range(len(CodeWords)-1 , -1, -1):
        if i >= M:
            CodeWords[i] = CodeWords [i - M]
        else:
            CodeWords[i] = -1

    EncodedCodewords = CodeWords[:]
    GeneratorPolynomial = CorrectionCode.code_generator(M)

    #N = len(EncodedCodewords)-len(GeneratorPolynomial)
    #for i in range(N):
    #    GeneratorPolynomial.append(0)

    #for i in range(len(GeneratorPolynomial)-1 , -1, -1):
    #    if i >= N:
    #        GeneratorPolynomial[i] = GeneratorPolynomial[i - N]
    #    else:
    #        GeneratorPolynomial[i] = 0

    N = len(EncodedCodewords) - 1
    ErrorCorrectionCode = EncodedCodewords[:]
    for i in range(len(EncodedCodewords)-M):
        if -1 != ErrorCorrectionCode[N]:
            K = ErrorCorrectionCode[N]
            for j in range(N - M, N+1):
                if ErrorCorrectionCode[j] != -1:
                    A = CorrectionCode.Alpha.alpha[ErrorCorrectionCode[j]]
                else:
                    A = 0
                if GeneratorPolynomial[j - (N-M)] != -1:
                    B = CorrectionCode.Alpha.alpha[(K + GeneratorPolynomial[j - (N-M)]) % 255]
                else:
                    B = 0
                ErrorCorrectionCode[j] = CorrectionCode.Alpha.map[A ^ B]
        N = N - 1



    CorrectionCodewords = []
    for i in range(M):
        CorrectionCodewords.append(CorrectionCode.Alpha.alpha[ErrorCorrectionCode[i]])
    CorrectionCodewords.reverse()
    DataCodewords = MessageCodewords + CorrectionCodewords

    DataBits = ''
    for i in range(len(DataCodewords)):
        DataBits = DataBits + Dec2Bin(DataCodewords[i], 8)
    DataBits = DataBits + '0'*7
    return DataBits
