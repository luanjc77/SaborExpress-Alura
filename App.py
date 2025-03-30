import os
#Dicionário no pyton, temos uma 'chave' e um 'valor
restaurantes = [
                {'nome': 'Praça','categoria': 'Japonesa','ativo': False}, 
                {'nome': 'Pizza Suprema','categoria': 'Pizza','ativo': True},
                {'nome': 'Cantina','categoria': 'Italiano','ativo': False}
            ]


def print_nome():
    '''Eseta Função tem o objetivo de printar o no em da aplicação'''
    print('Sabor Express')

def exibir_opcoes():
    '''Printar as oplções presente no App'''
    print('1-Cadastrar Restaurantes\n')
    print('2-Listar Restaurantes\n')
    print('3-Alternar Edstado do Restaurante Restaurantes\n')
    print('4-Sair\n')

def finaliza_app():
    '''Fechar a Aplicação'''
    exibir_subtitulo('Finalizando o APP!!')

def exibir_subtitulo(texto):
    '''Exibir o nome do módulo que foi escolhido pelo usuário
    Limpa o terminar para exibir somente o módulo que foi escolhido
    Texto -> O nome do módulo escolhido
    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()#deixando uma linha em branco

def voltar_ao_menu_principal():
    input('\nDigite algo para voltar ao menu principal\n')
    main()

def opcao_invalida():
    '''Informa que a opção escolhida não é correta e volta ao menu principal'''
    print('opção inválida')
    main()

def novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do novo restaurante que vc deseja cadastrair: ')
    categoria_restaurante = input(f'Digite em qual a categoria em que o retaurante {nome_do_restaurante} se enquadra: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria_restaurante,'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'Cadastrado {nome_do_restaurante} com sucesso')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')
    print(f"{'Nome do Restaurante'.ljust(35)} | {'Categoria'.ljust(22)} | Status")
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'-> Restaurante: {nome_restaurante.ljust(20)}  | Categoria: {categoria_restaurante.ljust(20)} | Status: {ativo}' )
    voltar_ao_menu_principal()

def alterar_estado_restaurante():
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']# o 'not' é uma palavra resenvada que invete o estado da variavel, se esta true viral false, se for false vira true
            mesnagem = f'O Restaurate {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mesnagem)
    if not restaurante_encontrado:
        print('O restaurate não foi encontrado')        
    voltar_ao_menu_principal()


def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Sua opcao escolhida foi: '))
        print(opcao_escolhida)
        if opcao_escolhida == 1:
            novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_estado_restaurante()
        elif opcao_escolhida == 4:
            finaliza_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    print_nome()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()