def area_triangulo (base, altura):
    return(base * altura) / 2

base = int(input('base do triângulo:'))
altura = int(input('altura do triângulo:'))

print ("A área do Triângulo é:", area_triangulo(base, altura))