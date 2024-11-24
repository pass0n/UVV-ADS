Celsius = [-2.3, 0, 10, -15, -1, 3, 50, 22, -5.1, 33, 87, -100]

conversor = [x * 9 / 5 + 32 for x in Celsius]

print("Lista de Temperaturas em Fahrenheit: ")
print(conversor)

conversor.sort()
print("\nLista de Temperaturas em Fahrenheit em ordem crescente: ")
print(conversor)

indice_usuario = int(input("\nInforme o índice de início para exibição: "))
print(conversor[indice_usuario:])
