print('SUMAR DOS NÚMEROS');

num1 = int(input('Dame el primer número '));
num2 = int(input('Dame el segundo número '));

res = num1 + num1;
print("La suma de {0} + {1} = {2}".format(num1, num2, res));

if num1 > num2:
    print("{} es mayor que {}".format(num1, num2));
else:
    print("{} es mayor que {}".format(num2, num1));

print("-----------NUEVO PROGRAMA---------------")

edad = int(input("Ingrese su edad "));
if edad > 18:
    print("ERES MAYOR DE EDAD :)");
elif edad == 18:
    print("TIENES 18 AÑOS!! :D");
else:
    print("NO ERES MAYOR DE EDAD ):")

'''AND, OR, NOT, <, >, <=, =>, |'''

valor1 = 200;
valor2 = 2;
valor3 = 1000;

if(valor1 > 1000 and valor2 > 2)or valor3 < 2000:
    print("resultado");