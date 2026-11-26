Espetos = {'Espetinho de Boi':16.00,
           'Espetinho de Mamilo':16.00,
           'Espetinho de Frango':14.00,
           'Espetinho de Porco':14.00,
           'Espetinho de Coração':14.00,
           'Espetinho de Medalhão Misto':20.00,
           'Espetinho de Medalhão de Boi':20.00,
           'Espetinho de Medalhão de Frango':20.00,
           'Espetinho de Kafta':14.00,
           'Espetinho de Kafta Apimentada':14.00,
           'Espetinho de Kafta com Queijo':14.00,
           'Espetinho de Charque':20.00,
           'Espetinho de Picanha':25.00,
           'Espetinho de Mamilão':25.00,
           'Espetinho de Contra Filé':20.00,
           'Espetinho de Alcatra':25.00,
           'Espetinho Pau Carnudo':25.00,
           }
Bebidas = {'Cerveja':{'Skol 600ml':12.00,'Brahma 600ml':10.00},
                'Refrigerante':{'Coca cola 1l':10.00,'Guaraná 1l':10.00}} # type: ignore
def menu():
    print('------Menu------')
    print('1-Espetinhos')
    print('2-bebidas')
    print('3-Destilados')
    print('4 -')
    print('0- sair')
def exibir_espetos():
    for nome , preco in Espetos.items():
        print(f'{nome} -----  R${preco:.2f}')
def exibir_cervejas(categoria):
    for nome , preco in Bebidas[categoria].items():
        print(f'{nome} -----  R${preco:.2f}')


while True:
    menu()
    opc = input('escolha uma opção:')
    if opc == '1':
       exibir_espetos()
    elif opc == '2':
        print('1 - Cervejas')
        print('2 - refrigerantes')
        resp = input('Escolha:')
        if resp == '1':
            exibir_cervejas('Cerveja')
        elif resp == '2':
            exibir_cervejas('Refrigerante')
        else:
            print('opcção inválida!')
    elif opc == '0':
        print('Progama encerrado')
        break
    else:
        print('Opção inválida!')
    