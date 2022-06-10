import pandas as pd

personas=pd.read_csv("C:\Users\User\Downloads\personas_2011 (2).csv", sep=";")

print(personas.head())
print(personas.info())
print(personas.descirbe())
#filtramos persons de sexo 1, con menor edad de 40
personas[(personas["sexo_id"]==1)&(personas["edad"]<40)]