#B
Year = int(input("Год"))
if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0):
    Days = 366
else:
    Days = 365

print(f"В году {Year} количество дней: {Days}") 