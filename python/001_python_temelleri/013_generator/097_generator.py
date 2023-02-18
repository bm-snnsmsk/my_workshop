def cube() :
    for i in range(10) :
        yield i ** 3

generator = cube()

print(next(iter(generator)))
print(next(iter(generator)))
print(next(iter(generator)))

while True :
    try :
        print(next(iter(generator)))
    except StopIteration :
        break