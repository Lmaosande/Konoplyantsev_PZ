try:
    a = int(input("Введите целое число"))
    b = int(input("Введите целое число"))
    c = int(input("Введите целое число"))
except ValueError:
    print("Нужно число ") 
if a > 0 or b > 0 or c > 0:
    print("Есть положительные числа")
else:
    print("Ни одного положительного")