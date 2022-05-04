def dos_programas(arch1, arch2,arch3):
    with open(arch1,"r") as f, open (arch2,"r") as a, open (arch3,"a") as af:
        for palabra in f.read():
            af.write(palabra)
        for letter in a.read():
            af.write(letter)
