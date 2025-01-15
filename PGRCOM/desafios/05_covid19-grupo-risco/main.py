doenca_pre_existente: bool = False
mulher_gravida: bool = False

idade = int(input("Informe sua idade: "))

doenca = str(
    input(
        "Possui alguma doença pré-existente, tipo asma, diabetes, hipertensão, ou câncer? S/n "
    ).upper()
)
if doenca not in ["S", "N"]:
    print("Informe apenas 'S' para sim ou 'N' para não.")
    exit()
elif doenca == "S":
    doenca_pre_existente = True

genero = str(input("Qual seu gênero? M = Masculino / F = Feminino ").upper())

if genero not in ["F", "M"]:
    print("Informe apenas 'F' para o gênero feminino ou 'M' para masculino.")
    exit()
elif genero == "F":
    gravida = str(input("Você está grávida? S/n ").upper())

    if gravida not in ["S", "N"]:
        print("Informe apenas 'S' para sim ou 'N' para não.")
        exit()
    elif gravida == "S":
        mulher_gravida = True


if idade >= 60 or doenca_pre_existente or mulher_gravida:
    print("Você faz parte do grupo de risco!")
else:
    print("Você não faz parte do grupo de risco!")


print(
    "Por favor, vamos evitar contato físico, não dividir copos e talheres, manter o ambiente arejado e higienizar sempre as mãos, superfícies e objetos."
)
