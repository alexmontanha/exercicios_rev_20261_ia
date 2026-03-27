valor_compra = float(input("Digite o valor da compra: "))

print(f"O valor da compra é: {valor_compra:.2f}")

taxa_desconto = 0.0

if valor_compra < 50:
    taxa_desconto = 0.0
elif (valor_compra < 100):
    taxa_desconto = 0.05
elif (valor_compra < 200):
    taxa_desconto = 0.10
else:
    taxa_desconto = 0.15

valor_desconto = valor_compra * taxa_desconto
valor_final = valor_compra - valor_desconto

print(f"A taxa de desconto é: {taxa_desconto:.2f}")
print(f"O valor do desconto é: {valor_desconto:.2f}")
print(f"O valor final da compra é: {valor_final:.2f}")