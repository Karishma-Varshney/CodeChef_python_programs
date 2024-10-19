# cook your dish here

import math

x,n = map(int,input().split())

total_laddu_price = n*10

money_left = x - total_laddu_price

total_jalebi = math.floor(money_left/20)

print(total_jalebi)
