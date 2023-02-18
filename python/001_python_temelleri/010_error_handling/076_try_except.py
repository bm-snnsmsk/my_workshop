try : 
    x = int(input('x : '))
    y = int(input('y : '))
    print(x/y)
except (ZeroDivisionError, ValueError, SyntaxError) as e:
    print("y 0 olamaz",e)
else : 
    print("herşy yoluda")