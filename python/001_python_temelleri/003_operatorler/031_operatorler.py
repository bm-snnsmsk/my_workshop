values = (10, 15, 25, 35, 49)
x,y,*z = values

a = b = [1,2,3]
c = [1,2,3]

print(type(values))
print(x,y,z)

print(f'a == b : {a == b}')
print(f'a == c : {a == c}')
print(f'a is b : {a is b}')
print(f'a is c : {a is c}')
print(f'35 in values : {35 in values}')
print(f'350 not in values : {350 not in values}')