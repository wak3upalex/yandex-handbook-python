name = input()
num = int(input())

gr_num = num // 100
pos_num = num % 10
bed_num = num // 10 % 10

print(f"Группа №{gr_num}.\n{pos_num}. {name}.\nШкафчик: {num}.\nКроватка: {bed_num}.")
