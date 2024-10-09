import math

# Number of test cases
t = int(input())

# Loop over each test case
for _ in range(t):
    a, b = map(int, input().split())
    tot = 0
    
    # Loop until Alice and Bob have the same number of slices
    while a != b:
        if a > b:
            x = math.ceil(a / 2)
            a -= x
        else:
            x = math.ceil(b / 2)
            b -= x
        tot += x
    
    # Print the total slices Charlie ate for this test case
    print(tot)
