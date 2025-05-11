print("Cauculadora de 7 operações!")
x = int(input("Escolha sua operação!\ndigite 1 para soma, 2 para subtração, 3 para divisão, 4 para multiplicação e 5 para raiz quadrada, 6 para potêntia, 7 para logaritimo. \n "))

if (x==1):
    a =  float(input("informe o primeiro número:"))
    b =  float(input("informe o segundo número:"))
    c = a + b
    print("o resultado da soma é:",c)
elif (x==2):
    d =  float(input("informe o primeiro número:"))
    e =  float(input("informe o segundo número:"))
    f = d - e
    print("o resultodo da subtração:", f)
elif (x==3):
    g =  float(input("informe o primeiro número:"))
    h =  float(input("informe o segundo número:"))
    i = g/h
    print("o resultado da divisão é:","%.2f"%i)
elif(x==4):
    j =  float(input("informe o primeiro número:"))
    k = float(input("informe o segundo número:"))
    l = j * k
    print("o resultado da multiplicação é:",l)
elif(x==5):
    m = float(input("informe o número:"))
    n = m**0.5
    print("a raiz é:",n)
elif(x==6):
    o = float(input("informe o número para base:"))
    p = float(input("informe o número da elevação:"))
    q= o**p
    print("o resultado da potenciação é:","%.2f"%q)
elif(x==7):
    import math
    def log_base_personalizado(x, base):
        return math.log(x) / math.log(base)
    numero = float(input("o numero: "))
    base = float(input("na base: "))
    resultado = log_base_personalizado(numero, base)

    print(f"Logaritmo de {numero} na base {base} é: {resultado}")
else:
    print("ainda não tem mais operação")
