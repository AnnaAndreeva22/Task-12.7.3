# Task-12.7.3

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = input("Введите сумму:")
TKB = 5.6
SKB = 5.9
VTB = 4.28
SBER = 4.0

money_1 = int(money)
deposit = (money_1*TKB/100, money_1*SKB/100, money_1*VTB/100, money_1*SBER/100)
deposit_1 = list(map(int, deposit))

text = input("Накопленные средства за год:")
print(deposit_1)

max_1 = max(deposit_1)
text_1 = input("Максимальная сумма, которую вы можете заработать:")
print(max_1)
