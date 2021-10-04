def generator():
    alpha = []
    alpha.append(1)
    for i in range(1, 255):
        alpha.append((alpha [i - 1] * 2)) if (alpha [i - 1] * 2) <= 255 else alpha.append((alpha [i - 1] * 2) ^ 285)
    return alpha

def map():
    alpha = generator()
    alpha_map = [-1]*256
    for i in range(len(alpha)):
        alpha_map[alpha[i]] = i
    return alpha_map