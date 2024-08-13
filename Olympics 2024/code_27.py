G,S,B = map(int,input().split())

gold = 5-G
silver = 5-S
bronze = 5-B

print(abs(gold+silver+bronze))
