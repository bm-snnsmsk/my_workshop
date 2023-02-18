while True :
    try : 
        x = int(input('x : '))
        y = int(input('y : '))
        print(x/y)
    except Exception as e:
        print("y 0 olamaz",e)
    else : 
        break
    finally :
        print("try except sonlandı")