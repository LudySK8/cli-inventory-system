# Lista vazia que vai guardar todos os produtos
estoque = []

# Função que procura um produto pelo código
def buscar_produto(codigo):# Pega um produto de cada vez do estoque
    for produto in estoque: # Se o código da ficha for igual ao que eu procuro...
        if produto["codigo"] == codigo: # ...devolvo a ficha e a função termina aqui
            return produto # Se o for acabou e não achei ninguém, devolvo "nada"
    return None

# Função da opção 1 do menu
def cadastrar_produto():
    # Pergunto o código e converto para número inteiro
    codigo = int(input("Codigo: ").strip())

    # Se achei alguém com esse código, ele já existe
    if buscar_produto(codigo) is not None:
        print("Erro: já existe um produto com esse código.")
        return  # saio da função e não cadastro nada

    # Pergunto o nome (já é texto, não preciso converter)
    nome = input("Nome: ").strip()
    # Pergunto o preço e converto para número com vírgula
    preco = float(input("Preco: ").strip())
    # Pergunto a quantidade e converto para inteiro
    quantidade = int(input("Quantidade: ").strip())

    # Se o preço OU a quantidade for negativo, não aceito
    if preco < 0 or quantidade < 0:
        print("Erro: preço e quantidade não podem ser negativos.")
        return  # saio da função sem guardar o produto

    # Monto a ficha do produto com o que a pessoa digitou
    produto = {
        "codigo": codigo,
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco,
    }
    # Coloco a ficha na lista do estoque
    estoque.append(produto)
    print("Produto cadastrado!")

# Função da opção 2 do menu
def calcular_total():
    # Começo o total em zero, igual a uma calculadora zerada
    total = 0
    # Pego um produto de cada vez do estoque
    for produto in estoque:
        # Somo a quantidade desse produto no total
        total = total + produto["quantidade"]
    # Mostro o resultado final
    print(f"Total de produtos em estoque: {total}")

# Função que mostra o menu e chama as outras funções
def menu():
    # Repete para sempre, até eu mandar parar com o break
    while True:
        print("\n1 - Cadastrar produto")
        print("2 - Calcular total de produtos em estoque")
        print("0 - Sair")
        # Leio a opção que a pessoa escolheu (como texto)
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            cadastrar_produto()   # chama a função de cadastro
        elif opcao == "2":
            calcular_total()      # chama a função do total
        elif opcao == "0":
            print("Encerrando.")
            break                 # quebra o while e o programa acaba
        else:
            print("Opção inválida.")  # qualquer outra coisa

# Começa o programa chamando o menu
menu()