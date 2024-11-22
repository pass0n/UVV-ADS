frase: str = input("Digite uma frase qualquer: ")

while len(frase) < 30:
    frase: str = input("Sua frase deve ter pelo menos 30 caracteres! Digite novamente: ")

contador = 0
caractere_contagem = input("Qual caractere deseja contar? ")

for caractere in frase:
    if caractere == caractere_contagem:
        contador += 1

print(f"O caractere '{caractere_contagem}' apareceu {contador} vezes na frase!")

pular_caractere = input("Escolha um caractere para pular ao imprimir a frase: ")
for caractere in frase:
    if caractere == pular_caractere:
        continue
    print(caractere)

encerrar_caractere = input("Escolha um caractere que vai parar a exibição da frase: ")
for caractere in frase:
    if caractere == encerrar_caractere:
        break
    print(caractere)
