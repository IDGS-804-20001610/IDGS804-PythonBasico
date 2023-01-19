listaa = [];
lista = list;

lista1 = ["Roberto", 1.2, 23, True];

print(lista1);

print(lista1[:]);
print(lista1[2:4]);
print(lista1[:2]);
print(lista1[3:]);

''''Agregar elemento al final de la lista'''
lista1.append("Carlos");
print(lista1);

''''Agregar elemento a la lista en la posición indicada'''
lista1.insert(0, "Mario");
print(lista1);

''''Agregar una lista a otra lista'''
lista1.extend([9, 10, 11]);
print(lista1);

'''Posición del elemento en cuestión'''
print(lista1.index("Carlos"));

'''Eliminación de un elemento'''
lista1.remove("Roberto");
print(lista1);

'''Extracción del último elemento'''
lista1.pop()
print(lista1);
