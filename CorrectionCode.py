import AlphaCode_generator 

def poly_multiply(poly, temp):
    result = []
    a = []
    b = [0]
    for i in range(len(poly)):
        a.append((poly[i] + temp[0]) % 255)
        b.append((poly[i] + temp[1]) % 255)

    ''' 
        a[1,0,2]
        b[0,1,0,2]
    '''
    result.append(a[0])
    for i in range(1, len(a)):
        a1 = Alpha.alpha[a[i]]
        b1 = Alpha.alpha[b[i]]
        result.append(Alpha.map[(a1 ^ b1)] % 255)
    result.append(b[len(b) - 1])
    return result


def code_generator(M):
    Temp = [0, 0]
    Poly = [0, 0]
    for i in range(1, M):
        Temp[0] = i
        Poly = poly_multiply(Poly, Temp)
    return Poly
            

class Alpha:
    map = AlphaCode_generator.map()
    alpha = AlphaCode_generator.generator()