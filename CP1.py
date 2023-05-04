# RM: RM99727 NOME: Lucas Feijó

boasVindas = int(input(f'Boas vindas a vinheiria Agnello! Como podemos ajudar? (Digite o número desejado) \n 1.Fazer o seu cadastro \n 2.Ver o catálogo \n 3.Valor do frete \n 4.Sair do atendimento'))
dadosVinhos = {
    'Vinho tinto': 50.00,
    'Vinho branco': 90.00,
    'Vinho rosé': 75.00,
    'Champagne': 110.00,
    'Espumante': 200.00,
}
precoVinhoTinto = dadosVinhos["Vinho tinto"]
precoVinhoBranco = dadosVinhos["Vinho branco"]
precoVinhoRosé = dadosVinhos["Vinho rosé"]
precoChampagne = dadosVinhos["Champagne"]
precoEspumante = dadosVinhos["Espumante"]

catalogo = f'\n Vinho tinto: R${precoVinhoTinto} \n Vinho Branco: R${precoVinhoBranco} \n Vinho Rosé: R${precoVinhoRosé} \n Champagne: R${precoChampagne} \n Espumante: R${precoEspumante}'

frete = 15.00

if boasVindas == 1 :
    nomeCompleto = input(f'Qual o seu nome completo?')
    idade = int(input(f'Qual a sua idade?'))
    if idade < 18 :
        print('Nos desculpe, mas vender vinho para uma pessoa menor de idade é crime!')

    elif idade >= 18 :       
        enderecoDoCliente = input(f'Qual o endereço do cliente?')
        opcaoDeEndereco = int(input(f'O endereço de entrega é a localização informada anteriormente? \n 1.Sim \n 2.Não'))

        if opcaoDeEndereco == 1 :
            enderecoDeEntrega = enderecoDoCliente
        
        if opcaoDeEndereco == 2 :
            enderecoDeEntrega = input(f'Qual o endereço de entrega?')

        if idade >= 18 :

            quantidades = {}
            for vinhos, preco in dadosVinhos.items():
                quantidade = int(input(f'Quantos {vinhos} voce deseja comprar?'))
                quantidades[vinhos] = quantidade
            print(quantidades)
            print(enderecoDeEntrega)

            valorTotal = 0
            for vinhos, quantidade in quantidades.items():
                valorTotal += dadosVinhos[vinhos] * quantidade
        
            if valorTotal <= 99 :
                print(f'Valor minímo para compra é de R$100,00 reais.')

            elif valorTotal >= 200 :
                print(f'Sua compra foi realizada com sucesso com o total no valor de {valorTotal}, seu frete foi por nossa conta!')

            else :
                valorTotalFrete = valorTotal + frete
                print(f'Sua compra foi realizada com sucesso com o total no valor de {valorTotalFrete}.')



if boasVindas == 2 :
    print(f'Esse é o catálogo de vinhos da casa: {catalogo}')

if boasVindas == 3 :
    print(f'Esta é o valor fixo do frete: R${frete}')

if boasVindas == 4 :
    print('Obrigado pela preferencia e volte sempre!')