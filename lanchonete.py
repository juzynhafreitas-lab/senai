print("=== Lá no charuri ===")
print(" " * 4, "lanchonete")

nome_cliente = input("Por favor, digite o seu nome: ")
print(f"Olá, {nome_cliente}")

print("=== NOSSO CARDÁPIO ===")
print("1. hambúrguer matador - R$39.59")
print("2. lanche natural - R$20.00")
print("3. caldo verde - R$38.00")
print("4. sopa de legumes - R$35.00")

print("\nFaça o seu pedido")

qtd_hamburguer = int(input("Quantidade de hambúrguer matador: "))
qtd_lanche_natural = int(input("Quantidade de lanche natural: "))
qtd_caldo_verde = int(input("Quantidade de caldo verde: "))
qtd_sopa_de_legumes = int(input("Quantidade de sopa de legumes: "))

# fechando a conta
total_hamburguer = qtd_hamburguer * 39.59
total_lanche_natural = qtd_lanche_natural * 20.00
total_caldo_verde = qtd_caldo_verde * 38.00
total_sopa_de_legumes = qtd_sopa_de_legumes * 35.00

# Exibindo o cupom fiscal
print("\n" + "=" * 30)
print(" " * 8 + "CUPOM FISCAL" + " " * 8)
print("=" * 30)
print(f"Cliente: {nome_cliente}")

valor_total = (
    total_hamburguer +
    total_lanche_natural +
    total_caldo_verde +
    total_sopa_de_legumes
)

print(f"Total do pedido: R$ {valor_total:.2f}")