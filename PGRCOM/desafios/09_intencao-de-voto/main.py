candidatos = ["Luleta Silveira", "Jamanta Sonaro", "Margarina Silvete"]

votacao = {}

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
sexo = ""

while sexo not in ["F", "M", "O"]:
    sexo = input("Digite seu sexo: \nM = Masculino\nF = Feminino\nO = Outro\n").upper()

if sexo == "M":
    sexo = "Masculino"
elif sexo == "F":
    sexo = "Feminino"
else:
    sexo = "Outro"

while True:
    print("\nEm qual candidato deseja votar? \n")
    for i, j in enumerate(candidatos):
        print(f"{i} - {j}")

    try:
        voto = int(input("\nDigite o número do candidato de sua escolha (0, 1 ou 2): "))

        if voto < 0 or voto >= len(candidatos):
            print("Voto inválido! Tente novamente.")
        else:
            print("\nVotação concluída com sucesso!")
            break
    except ValueError:
        print("Voto inválido! Por favor, insira um número válido.")

votacao[nome] = {"idade": idade, "sexo": sexo, "voto": candidatos[voto]}

print(f"\nIntenção de voto de {nome}:")
for nome, dados in votacao.items():
    print(f"\nNome: {nome}")
    print(f"Idade: {dados['idade']}")
    print(f"Sexo: {dados['sexo']}")
    print(f"Voto: {dados['voto']}")
