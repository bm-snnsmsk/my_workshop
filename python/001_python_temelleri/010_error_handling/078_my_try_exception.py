def check_pass(passw) :
    import re
    if len(passw) < 8 :
        raise Exception("parola en az 7 karakter olmalı")
    elif not re.search("[a-z]", passw) :
        raise Exception("parola en az bir küçük harf içermeli")
    elif not re.search("[A-Z]", passw) :
        raise Exception("parola en az bir büyük harf içermeli")
    elif not re.search("[0-9]", passw) :
        raise Exception("parola en az bir rakam içermeli")
    elif not re.search("[_@$]", passw) :
        raise Exception("parola en az bir alfanumerik içermeli")
    elif re.search("\s", passw) :
        raise Exception("parola boşluk içermemeli")
    else :
        print("parola doğru")

parola ="1533 36wA_ "

try :
    check_pass(parola)
except Exception as e:
    print(e)

