# cook your dish here
t = int(input())

while(t):
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    
    c1 = 0
    c2 = 0
    
    for i in range(3):
        if(a[i]>b[i]):
            c1 = c1+1 
            
        else:
            c2 = c2+1 
            
    if c1>c2:
        print('A')
        
    else:
        print('B')
        
    t = t-1     