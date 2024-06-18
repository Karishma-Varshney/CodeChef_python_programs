t = int(input())

while t > 0:
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # Your code goes here
    summ=0
    for i in range(len(a)):
        if a[i]>=x:
            summ=summ+b[i]
    print(summ)
    t -= 1
