#B. Описать фунуцию ShiftRight3(A,B,C), выпонлняющую правый циклический сдвиг.
def ShiftRight3(A, B, C):
    temp = A
    A = C
    C = B
    B = temp
    return A, B, C

A1, B1, C1 = 1.0, 2.0, 3.0
A2, B2, C2 = 4.0, 5.0, 6.0

A1, B1, C1 = ShiftRight3(A1, B1, C1)
A2, B2, C2 = ShiftRight3(A2, B2, C2)

print(A1, B1, C1)  
print(A2, B2, C2)  
