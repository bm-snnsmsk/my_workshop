def display_user(**params) : # parametreler dictionariden geleceğini belirtmek için **
    for k, v in params.items() :
        print('{} is {}'.format(k, v))  


display_user(name = 'sinan', age = 38)
display_user(name = 'baran', age = 2, city = 'silopi')
display_user(name = 'tubanur', age = 5, city = 'silopi', email = '5444494263')


print("-----------------------------------------")
def display_user2(a, b, *args, **kwargs) : 
    print(a)
    print(b)
    print('tuple değerler : ',args)
    print("dictionary değerler : ",kwargs)


display_user2(10, 20, 35, 56, name = 'tubanur', age = 5, city = 'silopi', email = '5444494263')


