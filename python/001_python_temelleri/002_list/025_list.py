txt = "hello there. my name is sinan"
liste1 = [100, 200, 300]
liste2 = ["sinan", "baran", "tuba", "emine"]

print(txt.split()[0])
print(liste1)
print(liste1 + liste2)
print([liste1, liste2])
print(len(liste1))
print(liste2[0])
print(liste2[-1])
liste2[2] = "tuba nur"
print(liste2)
print("sinan" in liste2)
print(liste2[::-1])
del liste2[-1]
print(liste2)
