#Atividade 1- Informar produto e receber o valor#

def valor(produto):
    if produto == 'salgado':
        return 4
    elif produto == 'refrigerante':
        return 4.5
    elif produto == 'suco':
        return 5
    elif produto == 'sorvete':
        return 6
    elif produto == 'cafe':
        return 4
    elif produto == 'capuccino':
        return 6
    elif produto == 'bolo':
        return 4.5
    elif produto == 'dadinho':
        return 0.5

pessoas = []
pedidos = []
v =[]
pessoa1 = str(input('Insira seu nome:'))
pessoas.append(pessoa1)
pedido1 = str(input('Insira seu pedido:'))
pedidos.append(pedido1)

pessoa2 = str(input('Insira seu nome:'))
pessoas.append(pessoa2)
pedido2 = str(input('Insira seu pedido:'))
pedidos.append(pedido2)

pessoa3 = str(input('Insira seu nome:'))
pessoas.append(pessoa3)
pedido3 = str(input('Insira seu pedido:'))
pedidos.append(pedido3)

pessoa4 = str(input('Insira seu nome:'))
pessoas.append(pessoa4)
pedido4 = str(input('Insira seu pedido:'))
pedidos.append(pedido4)

pessoa5 = str(input('Insira seu nome:'))
pessoas.append(pessoa5)
pedido5 = str(input('Insira seu pedido:'))
pedidos.append(pedido5)

pessoa6 = str(input('Insira seu nome:'))
pessoas.append(pessoa6)
pedido6 = str(input('Insira seu pedido:'))
pedidos.append(pedido6)

pessoa7 = str(input('Insira seu nome:'))
pessoas.append(pessoa7)
pedido7 = str(input('Insira seu pedido:'))
pedidos.append(pedido7)

    
def final():
    print(pessoas[0], '->', pedidos[0], '->',valor(pedido1))
    v.append(valor(pedido1))
    print(pessoas[1], '->', pedidos[1], '->',valor(pedido2))
    v.append(valor(pedido2))
    print(pessoas[2], '->', pedidos[2], '->',valor(pedido3))
    v.append(valor(pedido3))
    print(pessoas[3], '->', pedidos[3], '->',valor(pedido4))
    v.append(valor(pedido4))
    print(pessoas[4], '->', pedidos[4], '->',valor(pedido5))
    v.append(valor(pedido5))
    print(pessoas[5], '->', pedidos[5], '->',valor(pedido6))
    v.append(valor(pedido6))
    print(pessoas[6], '->', pedidos[6], '->',valor(pedido7))
    v.append(valor(pedido7))
    print(f'Valor final em caixa: R${v[0]+v[1]+v[2]+v[3]+v[4]+v[5]+v[6]}')
final()


    

