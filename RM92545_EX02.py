valor = float(input("Informe o valor do pacote: R$ "))
categoria = int(input("Informe a categoria (1-primeira classe, 2-executiva e 3-econõmica)  dos assentos: "))
quantidade = int(input("Informe a quantidade de viajantes: "))
desconto = 0.0
total = 0.0

if categoria == 1:
    if quantidade == 2:
        desconto = valor * 10 / 100
        total = valor - desconto
        print(f"Valor bruto R$ {valor:,.2f}, valor do desconto R$ {desconto:,.2f}, valor líquido R$ {total:,.2f}")
    elif quantidade == 3:
        desconto = valor * 15 / 100
        total = valor - desconto
        print(f"Valor bruto R$ {valor:,.2f}, valor do desconto R$ {desconto:,.2f}, valor líquido R$ {total:,.2f}")
    elif quantidade >= 4:
        desconto = valor * 10 / 100
        total = valor - desconto
        print(f"Valor bruto R$ {valor:,.2f}, valor do desconto R$ {desconto:,.2f}, valor líquido R$ {total:,.2f}")

elif categoria == 2:
    if quantidade == 2:
        desconto = valor * 5 / 100
        total = valor - desconto
        print(f"Valor bruto R$ {valor:,.2f}, valor do desconto R$ {desconto:,.2f}, valor líquido R$ {total:,.2f}")
    elif quantidade == 3:
        desconto = valor * 7 / 100
        total = valor - desconto
        print(f"Valor bruto R$ {valor:,.2f}, valor do desconto R$ {desconto:,.2f}, valor líquido R$ {total:,.2f}")
    elif quantidade >= 4:
        desconto = valor * 8 / 100
        total = valor - desconto
        print(f"Valor bruto R$ {valor:,.2f}, valor do desconto R$ {desconto:,.2f}, valor líquido R$ {total:,.2f}")

elif categoria == 3:
    if quantidade == 2:
        desconto = valor * 3 / 100
        total = valor - desconto
        print(f"Valor bruto R$ {valor:,.2f}, valor do desconto R$ {desconto:,.2f}, valor líquido R$ {total:,.2f}")
    elif quantidade == 3:
        desconto = valor * 4 / 100
        total = valor - desconto
        print(f"Valor bruto R$ {valor:,.2f}, valor do desconto R$ {desconto:,.2f}, valor líquido R$ {total:,.2f}")
    elif quantidade >= 4:
        desconto = valor * 5 / 100
        total = valor - desconto
        print(f"Valor bruto R$ {valor:,.2f}, valor do desconto R$ {desconto:,.2f}, valor líquido R$ {total:,.2f}")

else:
    print("Categoria inválida!")

