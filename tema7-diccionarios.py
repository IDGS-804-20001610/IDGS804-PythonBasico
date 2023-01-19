miDiccionario = {"Matricula": 20001610, "Apellido": "Ruiz"}

print(miDiccionario["Apellido"]);

'''Agragar un campo y valor al diccionario'''
miDiccionario["Materia"] = "DWP";
print(miDiccionario);

'''Modificar un valor'''
miDiccionario["Matricula"] = 20002730;
print(miDiccionario);

'''Eliminar ese elemento/campo del diccionario'''
del miDiccionario["Apellido"];
print(miDiccionario);