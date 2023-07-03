#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros
print("{:=^40}".format("LOJA"))
preço = float(input("Preço das compras: R$"))
print("""FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão""")
opção = int(input("Qual é a opção? "))
if opção == 1:
    total = preço * 0.9
elif opção == 2:
    total = preço * 0.95
elif opção == 3:
    total = preço
    parcela = total / 2
    print("Sua compra será parcelada em 2 vezes de R${:.2f}".format(parcela))
elif opção == 4:
    total = preço * 1.2
    totparc = int(input("Qualtas parcelas? "))
    parcela = total / totparc
    print("Sua compra será parcelada em {} vezes de R${:.2f} COM JUROS".format(totparc, parcela))
else:
    total = preço
    print("OPÇÃO INVÁLIDA de pagamento. Tente novamente!")
print("Sua compra de R${:.2f} vai custar R${:.2f} no final".format(preço, total))
