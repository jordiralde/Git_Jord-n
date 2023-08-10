'''
print("inicio")

rango = int(input("rango del for: "))

for i in range(rango):
    print("*" * (i+1))

print("fin")
'''

estrella = '*'
rango = int(input("rango del for: "))

for i in range(rango):
    print(estrella)
    estrella = estrella * 2