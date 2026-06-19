from modelos import Produto, listar_produtos

def exibir_menu():
    print(""" 
===================================
          EXIBIR MENU
===================================
[1] - Listar 
[2] - Cadastrar
[0 ]- Sair
===================================
""")
    
def cadastrar():
    nome = input("Digite o nome: ")
    preco = float(input("Digite o preço: "))
    categoria = input("Digite a Categoria: ")  

    produto = Produto(nome, preco, categoria)
    produto.salvar()

def mostrar():
    for produto in listar_produtos():
        produto.exibir()

while True:
    exibir_menu()
    op = input("Digite uma opçao: ")
    if op == "0": break
    elif op == "1":
        mostrar()
    elif op == "2":
        cadastrar()
    else : print("Valor invalidade!")