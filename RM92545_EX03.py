membros = 5
voto_playstation = 0
voto_xbox = 0
voto_nintendo = 0

for x in range(membros):
    voto = (input('Informe seu voto "PLAYSTATION", "XBOX" OU "NINTENDO": '))
    voto = voto.upper()

    if voto == "PLAYSTATION":
        voto_playstation = voto_playstation + 1
    elif voto == "XBOX":
        voto_xbox = voto_xbox + 1
    elif voto == "NINTENDO":
        voto_nintendo = voto_nintendo + 1

if voto_playstation > voto_xbox and voto_playstation > voto_nintendo:
    print(f"PLAYSTATION foi escolhido com {voto_playstation} voto(s)")
elif voto_playstation == voto_xbox and voto_playstation > voto_nintendo:
    print(f"Deu empate! PLAYSTATION {voto_playstation} votos e XBOX {voto_xbox} votos")
elif voto_playstation == voto_nintendo and voto_playstation > voto_xbox:
    print(f"Deu empate! PLAYSTATION {voto_playstation} votos e NINTENDO {voto_nintendo} votos")
elif voto_xbox > voto_playstation and voto_xbox > voto_nintendo:
    print(f"XBOX foi escolhido com {voto_xbox} voto(s)")
elif voto_xbox == voto_nintendo and voto_xbox > voto_playstation:
    print(f"Deu empate! XBOX {voto_xbox} votos e NINTENDO {voto_nintendo} votos")
elif voto_nintendo > voto_playstation and voto_nintendo > voto_xbox:
    print(f"NINTENDO foi escolhido com {voto_nintendo} votos()")
