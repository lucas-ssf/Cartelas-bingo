print('==================> Bingo! <==================')
numero_cartelas = int(input('Entre com o número de cartelas: '))
numero_elementos = int(input('Entre com o número de elementos por cartela: '))

lista_cartelas = []
lista_sorteados = []

print('\n\n')
for i in range(numero_cartelas):
    print(f'Cartela {i}:')
    lista = []
    ident = input('\tEntre com o id: ')
    for j in range(numero_elementos):
        lista.append(int(input(f'\tElemento {j}: ')))
    cartela = [0, lista, ident]
    lista_cartelas.append(cartela)

print('\n\nSuas cartelas:')
for i, cartela in enumerate(lista_cartelas):
    print(f'{i}.Cartela {cartela[2]}: {cartela[1]}')

input('Pressione Enter...')
from time import sleep

sleep(2)

import platform
from os import system

i = 0
lista = []
while (True):
    if platform.system() == 'Windows':
        system("cls")
    else:
        system("clear")
    print(f'Partida {i}:\nNúmeros sorteados: {lista_sorteados[-1::-1]}')
    numero_sorteado = int(input('Digite o número sorteado: '))
    lista_sorteados.append(numero_sorteado)
    for cartela in lista_cartelas:
        if numero_sorteado in cartela[1]:
            cartela[0] += 1
        if cartela[0] == numero_elementos:
            print('BINGO >> ', end=' ')
        print(f'Cartela {cartela[2]}: {cartela[0]} | {[num for num in cartela[1] if num in lista_sorteados]}')
    print('\n')
    lista_cartelas.sort(reverse=True)
    i += 1

    if numero_sorteado < 0:
        lista_sorteados = []
        i = 0
        for cartela in lista_cartelas: cartela[0] = 0