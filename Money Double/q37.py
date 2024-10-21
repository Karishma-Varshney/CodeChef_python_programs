# cook your dish here
for i in range(int(input())):
    x,y=map(int,input().split())
    
    for i in range(y):
        if x<=1000:
            x+=1000
        else:
            x=2*x
            
    print(x)
