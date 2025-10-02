import random 

def es_camaleon(numero):
    """
    verifica si un numero es camaleon segun las condiciones:
    1. La suma de sus digitos es par 
    2. El numero invertido es divisible por 3
    """
    str_numero = str(numero)

    suma_digitos = sum(int(digito) for digito in str_numero)
    condicion1 = (suma_digitos % 2 == 0)

    numero_invertido = int(str_numero[::-1])
    condicion2 = (numero_invertido $ 3 == 0)

    return condicion1 and condicion2

def main():
    try:
    cantidad =

int(input("cantidad de numeros para validar: "))
      if  cantidad <= 0:
      print("La cantidad debe ser un numero positivo.")
        return
    except valueError:
        print("por favor, ingrese un numero valido.")
        return

    numeros_generados = []
    for _ in range(cantidad):

    numero = random.randint(100, 99999)

    numeros_generados.append(numero)

print("numeros generados:", ",.join(map(str, numeros_generados)))

print (Resultados:")
for numero in numeros_generados:
    if es_camaleon(numero):
        resultado = "s1"
    else:
        resultado = "no"
print(f"{numero}" -> {resultado} )

if __name__ == "__main__":
    main()
