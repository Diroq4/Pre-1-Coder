"""
Registra usuario.
"""
def register():
    user = input(f"Register your user: ")
    password = input(f"Register your password: ")
    return user, password

"""
Crea el diccionario vacio para guardar los datos.
"""
db = {}

user, password = register()
db["user"] = user
db["password"] = password
print("Successfully register!")

"""
Lee el guarda el diccionario en un archivo txt
"""
import json
with open("db.txt","a") as data_base:
    data_base.write()

with open("db.txt", "r") as data_base:
     full_data = data_base.read()