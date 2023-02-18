liste = ["1","2","5a","10b","abc",'15',1254]

"""  1. yöntem 
def isNumeric(val) :
    import re 
    if re.search('[^0-9]',val) :
        return False
    else :
        return True



numeric = []

for i in liste :
    if isNumeric(i) :
        numeric.append(i)

print(numeric) 

"""

## 2. yöntem
for i in liste :
    try :
        result = int(i) 
        print(result)
    except ValueError :
        continue

