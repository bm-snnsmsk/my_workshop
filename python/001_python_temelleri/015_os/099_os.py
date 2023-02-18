import os  
import datetime  

# result = dir(os)
# result = os.name

# os.chdir("..")
# result = os.getcwd()
# os.mkdir("../../klasor_deneme2333")
# os.makedirs("../../klasor_deneme2/a/b")

# result = os.listdir()
# result = os.listdir("C:\\")

# for i in os.listdir() :
#     if i.endswith(".py") :
#         print(i)

#result = os.stat("099_os.py")

#os.system('notepad.exe')

# os.rename('klasor_deneme',"yeni_klasor")

# os.removedirs("klasor_deneme3/ic/icerde")

result = os.path.abspath("099_os.py")
result = os.path.dirname("C:/xampp/htdocs/CyberSecurity/python/python_kurs/015_os/099_os.py")
result = os.path.basename("C:/xampp/htdocs/CyberSecurity/python/python_kurs/015_os/099_os.py")
# result = os.getcwd()

result = os.path.exists("C:/xampp/htdocs/CyberSecurity/python/python_kurs/015_os/099_os.py")
result = os.path.isdir("C:/xampp/htdocs/CyberSecurity/python/python_kurs/015_os/099_os.py")
result = os.path.isfile("C:/xampp/htdocs/CyberSecurity/python/python_kurs/015_os/099_os.py")

result = os.path.join("pyhton", "python_kurs","016_regexp")
result = os.path.split("C:\\deneme")
result = os.path.splitext("C:/xampp/htdocs/CyberSecurity/python/python_kurs/015_os/099_os.py")

print(result)