#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit
c = float(input("Informe a temperatura em ºC: "))
f = 9 * c / 5 + 32
print("A temperatura de {:.2f}ºC corresponde a {:.2f}ºF!".format(c, f))
