n = input("Мы будем проверять теорию коллатца. Введите число")

def collatz(num):
    num = int(num)
    if not num: return None
    while num != 1:
        num = num/2 if num % 2 == 0 else 3*num + 1

collatz(n)
