# cook your dish here

a,b,c,x = map(int,input().split())

vol_of_cuboid = a*b*c 

vol_of_cube = x**3 

if vol_of_cuboid > vol_of_cube:
    print('Cuboid')
    
elif vol_of_cuboid < vol_of_cube:
    print('Cube')
    
else:
    print('Equal')
    
