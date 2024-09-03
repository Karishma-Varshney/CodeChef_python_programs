# cook your dish here

x,y,k = map(int,input().split())

a = abs(x-y)

if a<=k:
    print('Yes')
    
else:
    print('No')
