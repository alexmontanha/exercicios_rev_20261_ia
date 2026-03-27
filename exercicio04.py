nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

print(f"A primeira nota é: {nota1}")
print(f"A segunda nota é: {nota2}")

media = (nota1 + nota2) / 2

print(f"A média é: {media:.2f}")

if media >= 7.0:
    print("Aprovado")
elif media < 5.0:
    print("Reprovado")
else:
    print("Recuperação")
    nota_recuperacao = float(input("Digite a nota de recuperação: "))
    print(f"A nota de recuperação é: {nota_recuperacao}")
    if nota_recuperacao >= 6.0:
        print("Aprovado")
    else:
        print("Reprovado")
