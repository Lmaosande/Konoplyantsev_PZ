#B
while True:
    try:
        N = int(input("Введите целое число N (N > 1): "))
        if N > 1:
            break
        else:
            print("N должно быть больше 1.")
    except ValueError:
        print("Введите целое число.")

K = 0
sum_K = 0
while sum_K < N:
    K += 1
    sum_K += K
print(f"Наименьшее K: {K}")
print(f"Сумма 1+2+...+K: {sum_K}")
