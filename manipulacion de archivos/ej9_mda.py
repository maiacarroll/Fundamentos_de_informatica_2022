def word_counter (arch):
    frecuencias={}
    with open(arch,"r") as arc:
        word_list=arc.read().split()
        for palabra in word_list:
            if palabra in frecuencias:
                frecuencias[palabra]+=1
            else:
                frecuencias[palabra]=1
            for word in frecuencias.keys():
                frecuencias[word] = round(frecuencias[word] / len(word_list), 3)