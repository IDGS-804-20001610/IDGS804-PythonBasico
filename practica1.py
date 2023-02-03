print('TABLA DE MULTIPLICAR');

def multi(num):
    for x in range(1, 11):
        print(f"{num} X {x} = {num * x}");

num = int(input("Deme un número: "));

multi(num);
