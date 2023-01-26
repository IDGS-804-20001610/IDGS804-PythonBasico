import os
class Operabas():
    #Propiedades de clase
    num1 = 0;
    num2 = 0;
    res = 0;

    #Constructor de la clase
    def __init__(self, a, b):
        self.num1 = a;
        self.num2 = b;

#'''LLEVA SELF SOLAMENTE CUANDO SON MÉTODOS / CONSTRUCTORES DE LA CLASE'''
    def suma(self):
        self.res = self.num1 + self.num2;

    def resta(self):
        self.res = self.num1 - self.num2;

def main():
    #Cuando se declara el cosntructor, el constructor espera los parametros
    os.system('cls')
    obj = Operabas(3, 4)
    obj.suma()
    print("La suma es: {}".format(obj.res));

if __name__ == '__main__':
    main()

    #Métodos de clase
