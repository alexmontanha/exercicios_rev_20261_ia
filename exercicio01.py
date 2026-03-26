# IMC = peso / (altura ** 2)
# Pedir o peso
# Pedir a altura

peso = float(input("Digite o seu peso (KG): "))
altura = float(input("Digite a sua altura (Mts): "))

imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc < 25:
    print("Classificação: Peso normal")
elif imc < 30:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obesidade")