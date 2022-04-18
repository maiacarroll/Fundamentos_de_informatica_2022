def susti (arch1,arch2):
    with open(arch1, "r") as f, open (arch2,"w") as a:
        for palabra in f.read():
            for letra in palabra:
                a.write(letra.replace(letra,letra + "\n"))

print(susti("bio.txt","images"))
str.replace --> (lo q uiero cambiar, lo q quiero q quede)