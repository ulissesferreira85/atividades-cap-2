idade = int(input("Informe sua idade: "))
bpm = int(input("Informe seu número de Batimentos Por Minuto (BPM): "))

if idade <= 2:
    if bpm < 120:
        print("Seu número de Batimentos Por Minuto está ABAIXO da faixa adequada.")
    elif bpm <= 140:
        print("Seu número de Batimentos Por Minuto está DENTRO da faixa adequada.")
    else:
        print("Seu número de Batimentos Por Minuto está ACIMA da faixa adequada.")

elif idade >= 8 and idade <= 17:
    if bpm < 80:
        print("Seu número de Batimentos Por Minuto está ABAIXO da faixa adequada.")
    elif bpm <= 100:
        print("Seu número de Batimentos Por Minuto está DENTRO da faixa adequada.")
    else:
        print("Seu número de Batimentos Por Minuto está ACIMA da faixa adequada.")

elif idade >= 18 and idade <= 65:
    if bpm < 70:
        print("Seu número de Batimentos Por Minuto está ABAIXO da faixa adequada.")
    elif bpm <= 80:
        print("Seu número de Batimentos Por Minuto está DENTRO da faixa adequada.")
    else:
        print("Seu número de Batimentos Por Minuto está ACIMA da faixa adequada.")

else:
    if bpm < 50:
        print("Seu número de Batimentos Por Minuto está ABAIXO da faixa adequada.")
    elif bpm <= 60:
        print("Seu número de Batimentos Por Minuto está DENTRO da faixa adequada.")
    else:
        print("Seu número de Batimentos Por Minuto está ACIMA da faixa adequada.")
