import os 
#NOMBRE DEL RESPOSITORIO = NOMBRE DE LA CARPETA
class Operabas():
    num1 = 0;
    num2 = 0;
    res = 0;
    menu = 0;

    def __init__(self, a, b):
        self.num1 = a;
        self.num2 = b;

    def suma(self):
        self.res = self.num1 + self.num2;

    def resta(self):
        self.res = self.num1 - self.num2;

    def multiplicacion(self):
        self.res = self.num1 * self.num2;

    def division(self):
        self.res = self.num1 / self.num2;


def main():
    menu=0
    while menu != 5:
        menu = int(input('INDICA EL NÚMERO DE LA OPERACIÓN QUE DESEAS REALIZAR: \n1. SUMAR \n2. RESTAR \n3. MULTIPLICAR \n4. DIVIDIR \n5. SALIR '));
        if menu == 1:
            print("SUMA")
            x = int(input('Dame el primer número: '));
            y = int(input('Dame el segundo número: '));
            obj = Operabas(x, y);
            obj.suma();
            print("La SUMA es: {}".format(obj.res));
        if menu == 2:
            x = int(input('Dame el primer número: '));
            y = int(input('Dame el segundo número: '));
            obj = Operabas(x, y);
            obj.resta();
            print("La RESTA es: {}".format(obj.res));
        if menu == 3:
            x = int(input('Dame el primer número: '));
            y = int(input('Dame el segundo número: '));
            obj = Operabas(x, y);
            obj.multiplicacion();
            print("La MULTIPLICACIÓN es: {}".format(obj.res));
        if menu == 4:
            x = int(input('Dame el primer número: '));
            y = int(input('Dame el segundo número: '));
            obj = Operabas(x, y);
            obj.division();
            print("La DIVISIÓN es: {}".format(obj.res));

if __name__ == '__main__':
    main()
