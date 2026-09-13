# Sistema de desconto

valor = float(input("Digite qual foi o valor da compra:"))

if valor < 200:
    desconto = 0.05
    resposta_desconto = "5%"
elif valor >= 300:
    desconto = 0.15
    resposta_desconto = "15%"
else:
    desconto = 0.10
    resposta_desconto = "10%"

total = ((valor) * (1.00 - desconto))

# Resposta
print(f"Parabéns! Você recebeu um desconto de {resposta_desconto}, o valor total será: R${total:.2f}.")
