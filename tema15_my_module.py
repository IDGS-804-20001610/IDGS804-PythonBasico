
def tem1():
    print("Hola desde my_module.py");

def tem2():
    print("Adiós desde my_module.py");

def main():
    print("Hola desde main");
    tem1()
    tem2()

if __name__=='__main__':
    main()