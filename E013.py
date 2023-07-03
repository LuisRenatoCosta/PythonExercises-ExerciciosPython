#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
salario = float(input("Qual o salário do funcionário? R$"))
novo = salario*1.15
print("Um salário que ganhava {:.2f}, com 15% de aumento, passa a receber R${:.2f}".format(salario, novo))
