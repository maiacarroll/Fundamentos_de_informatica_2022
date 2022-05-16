import requests
pedido = requests.get("https://macowins-server.herokuapp.com/prendas/1") # al ppio desps / 1
#vamos a  hacer un pedido, accediendo a la base de daros de la aplicacion
print(pedido)
#nos da una respuesta --> el canal de comunicacion funca
#json --> diccionario de python --> tipo de formato en el que el servidor nos devuelve las cosas
print(pedido.json())
#pq la de devuelve en este formato --> aplicacion RES --> responsible.. es una app en la cual
# se correlaciona los URL con los verbos HTTPS
#get --> verbo de http --> recursos q yo pido --> es el verbo que me trae un recurso
# url --> informatica y se relaciona con https --> una buena te brinda esta info con solo verla
#http --> tiene verbos que se relacionan

pedido1= requests.get("https://macowins-server.herokuapp.com/prendas/")
print(pedido1.json())
### ahaora sin el 1 me da un diccionario
pedido2= requests.get("https://macowins-server.herokuapp.com/prendas/7")
print(pedido2.json())

print(len(pedido1.json())) ## con esto averiguo --> cant de recursos en la app / de prendas
## solo funciona si se lo hago al root, es decir al /prendas

##url tienen que estar bien escritas semanticamente
# si quieero ver si tiene 400
pedido400=  requests.get("https://macowins-server.herokuapp.com/prendas/400")
print(pedido400)
## error 404 -->  status code
#               no pudo conectar, no pudo traer las cosas
             ## error --> no se puede conectar
## cada vez que yo hgao un pedido siempre viene --> status code , informacion en json ( a veces no siempre --> lo tengo que imprimir yo ),
# json trae la info del pedido , 

print(pedido1.headers) # toda la metadata --> la informacion de ese pedido --> la fecha - que tipo de info trae )

print(pedido1.status_code) #atributo de ese pedido


##https://http.cat/

peididod= requests.get('https://macowins-server.herokuapp.com/ventas')
print(peididod)
hshdos= requests.get('https://macowins-server.herokuapp.com/ventas/2)')
print(hshdos)

remera= requests.get('https://macowins-server.herokuapp.com/prendas?remeras')
print(remera)