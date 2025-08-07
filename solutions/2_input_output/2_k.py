num = int(input())
n1 = num // 1000
n2 = num // 100 % 10
n3 = num // 10 % 10
n4 = num % 10
print(f"{n2}{n1}{n4}{n3}")
