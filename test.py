import json
import urllib.request

# json_text = """
# [
#     { "id": 0, "nombre": "Remera Halloween", "precio": 1500 },
#     { "id": 1, "nombre": "Remera Navidad", "precio": 2000 }
# ]
# """

# diccionario = json.loads(json_text)
# print(type(diccionario))
# print(type(json_text))
# print(diccionario[0])
# print((diccionario[0]["nombre"]))

# for i in diccionario:
#     print(i["id"], end=" - ")
#     print(i["nombre"], end=" - $")
#     print(i["precio"])


# ///////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////


# nuevoString = ""

# urlhandler = urllib.request.urlopen("https://www.mockachino.com/fb1339e6-c1d4-48/users")

# for i in urlhandler:
    # print(type(i))
    # print(i)
    # print(type(i.decode()))
    # print(i.decode())
#     nuevoString = nuevoString + i.decode()

# print(type(nuevoString))
# print(nuevoString)

# arrayJson = json.loads(nuevoString)
# print(type(arrayJson))
# print(arrayJson)

# for i in arrayJson["users"]:
#     print(i["first_name"])


# ///////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////
# Manera elegante

urlhandler = urllib.request.urlopen("https://www.mockachino.com/fb1339e6-c1d4-48/users")
for i in urlhandler:
    arrayJson2 = json.loads(i)

print(type(arrayJson2))
print(arrayJson2)

for i in arrayJson2["users"]:
    print(i["first_name"])
