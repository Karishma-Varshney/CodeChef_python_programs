# cook your dish here
t = int(input())

for i in range(t):
    
    x = int(input())
    
    total_budget = (2**7 - 1)
    
    if total_budget <= x:
        print('YES')
        
    else:
        print('NO')