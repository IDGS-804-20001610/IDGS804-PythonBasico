
num1 = 10
num2 = 0

res = num1/num2;

try: 
    res = num1/num2
except ZeroDivisionError:
    print("Error en el programa")
finally:
    pass

print("Fin del programa")