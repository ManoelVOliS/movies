import csv
import random

def adicionarItem(nomeArquivo):
    while True:
        item = input("Digite um nome ou filme para adicionar (ou 'sair' para finalizar): ")
        if item.lower() == 'sair':
            break
        with open(nomeArquivo, mode='a', newline='') as arquivoCsv:
            escritorCsv = csv.writer(arquivoCsv)
            escritorCsv.writerow([item])
        print(f"'{item}' adicionado à lista.")

def sortearItem(nomeArquivo, assistidosArquivo):
    itens = []
    
    with open(nomeArquivo, mode='r') as arquivoCsv:
        leitorCsv = csv.reader(arquivoCsv)
        for linha in leitorCsv:
            if linha:
                itens.append(linha[0])
    
    if itens:
        sorteado = random.choice(itens)
        print(f"Item sorteado: {sorteado}")
        
        isFilme = input(f"O item '{sorteado}' é um filme? (s/n): ").lower()
        if isFilme == 's':
            itens.remove(sorteado)
            
            with open(nomeArquivo, mode='w', newline='') as arquivoCsv:
                escritorCsv = csv.writer(arquivoCsv)
                for item in itens:
                    escritorCsv.writerow([item])
            
            with open(assistidosArquivo, mode='a', newline='') as arquivoAssistidos:
                escritorCsv = csv.writer(arquivoAssistidos)
                escritorCsv.writerow([sorteado])
            print(f"Filme '{sorteado}' movido para a lista de assistidos.")
    else:
        print("A lista está vazia. Nenhum item para sortear.")

def removerItem(nomeArquivo):
    itens = []
    
    with open(nomeArquivo, mode='r') as arquivoCsv:
        leitorCsv = csv.reader(arquivoCsv)
        for linha in leitorCsv:
            if linha:
                itens.append(linha[0])

    if not itens:
        print("A lista está vazia. Nenhum item para remover.")
        return

    print("\nItens disponíveis para remover:")
    for i, item in enumerate(itens, 1):
        print(f"{i}. {item}")

    try:
        escolha = int(input("Escolha o número do item que deseja remover: "))
        if 1 <= escolha <= len(itens):
            itemRemovido = itens.pop(escolha - 1)
            
            with open(nomeArquivo, mode='w', newline='') as arquivoCsv:
                escritorCsv = csv.writer(arquivoCsv)
                for item in itens:
                    escritorCsv.writerow([item])
            print(f"Item '{itemRemovido}' removido da lista.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida. Digite um número.")

nomeArquivo = 'listaNomes.csv'
assistidosArquivo = 'filmesAssistidos.csv'

def main():
    while True:
        print("\nMenu:")
        print("1. Adicionar nomes ou filmes à lista")
        print("2. Sortear um item aleatoriamente")
        print("3. Remover um item da lista")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionarItem(nomeArquivo)
        elif escolha == '2':
            sortearItem(nomeArquivo, assistidosArquivo)
        elif escolha == '3':
            removerItem(nomeArquivo)
        elif escolha == '4':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()
