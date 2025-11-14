# Função para realização dos cálculos de divisão para cada tipo de produção, envase/expedição.
def quantidade_correta (opcao_linha, quantidade_producao, peso_bag_sacaria_expedicao):
    if opcao_linha == 1:
        total_bag_sacaria = (2000 * quantidade_producao) / peso_bag_sacaria_expedicao
    elif opcao_linha == 2:
        total_bag_sacaria = (1000 * quantidade_producao) / peso_bag_sacaria_expedicao
    elif opcao_linha == 3 or opcao_linha == 4:
         total_bag_sacaria = (2000 * quantidade_producao) / peso_bag_sacaria_expedicao
    elif opcao_linha == 5:
         total_bag_sacaria = (2000 * quantidade_producao) / peso_bag_sacaria_expedicao
    elif opcao_linha == 6:
        total_bag_sacaria = (2000 * quantidade_producao) / peso_bag_sacaria_expedicao
    elif opcao_linha == 7:
        total_bag_sacaria = (2000 * quantidade_producao) / peso_bag_sacaria_expedicao 
    elif opcao_linha == 8:
        total_bag_sacaria = (1000 * quantidade_producao) / peso_bag_sacaria_expedicao
    elif opcao_linha == 9:
        total_bag_sacaria = (1000 * quantidade_producao) / peso_bag_sacaria_expedicao                       
    else:
        total_bag_sacaria = 0
    return total_bag_sacaria  

# Formatador de valores, padrão brasileiro
def formata_br(valor, casas_decimais=2, dividir_por_mil=False):
    if dividir_por_mil:
        valor = valor / 1000
    formato = f"{valor:,.{casas_decimais}f}"
    formato = formato.replace(",", "X").replace(".", ",").replace("X", ".")
    return formato
   
# Menu de opções
print('\n∷ MENU QUANTIDADE CORRETA POR DESTINO:\n')

print('[1] Bag Ruminantes')
print('[2] Bag Pet/Peixes')
print('[3] Sac Ruminates')
print('[4] Sac Aves/Suinos')
print('[5] Sac Pet/Peixes')
print('[6] Exp Granel Ruminantes')
print('[7] Exp Granel Aves/suinos')
print('[8] Exp Granel Pet/PEixes')
print('[9] Envase Cães\n')

# Condição de escolha e filtro
opcao_linha = int(input('Digite uma opção: '))
if opcao_linha in (1, 2):
    quantidade_producao = int(input('Quantas Bateladas?: '))
    peso_bag_sacaria_expedicao = int(input('Qual o peso de cada bag?: '))
elif opcao_linha in (3, 4):
    quantidade_producao = int(input('Qunatas bateladas?: '))
    peso_bag_sacaria_expedicao = int(input('Qual o peso de cada sacaria?: '))
elif opcao_linha == 5:    
  quantidade_producao = int(input('Qunatas bateladas?: '))
  peso_bag_sacaria_expedicao = int(input('Qual o peso de cada sacaria?: '))
elif opcao_linha == 6:
  quantidade_producao = int(input('Qunatas bateladas?: '))
  peso_bag_sacaria_expedicao = 1
elif opcao_linha == 7:
  quantidade_producao = int(input('Qunatas bateladas?: '))
elif opcao_linha == 8:  
  quantidade_producao = int(input('Qunatas bateladas?: '))
elif opcao_linha == 9:
  quantidade_producao = int(input('Qunatas bateladas?: '))
  peso_bag_sacaria_expedicao = int(input('Qual o peso de cada pacote?: ')) 
else:
    print('Opção inválida')  

# Armazenamento do resultado da função
resultado = quantidade_correta (opcao_linha, quantidade_producao, peso_bag_sacaria_expedicao)

# Mostrando o resultado para o usuário
if opcao_linha == 1:
    print(f'Em uma produção de {quantidade_producao} bateladas na linha de Ruminates, o total a ser retirado do silo 80701 é de {formata_br(resultado)} Bags')
elif opcao_linha == 2:
    print(f'Em uma produção de {quantidade_producao} bateladas na linha Pet/Peixes, o total de Big Bag no silo 90907 é de {formata_br(resultado)}')
elif opcao_linha == 3:
    print(f'Em uma produção de {quantidade_producao} bateladas na linha Ruminates, o total de Sacarias a ser tirado é de {formata_br(resultado)}')
elif opcao_linha == 4:
    print(f'Em uma produção de {quantidade_producao} bateladas na linha Aves/Suinos, o total de Sacarias a ser tirado é de {formata_br(resultado)}')
elif opcao_linha == 5:
    print(f'Em produção de {quantidade_producao} bateladas na linha Pet/Peixes, o total de Sacarias a ser tirado é de {formata_br(resultado)}') 
elif opcao_linha == 6:
    print(f'Em uma produção de {quantidade_producao} bateladas na linha Ruminates, o total para o Granel Ruminates é de {formata_br(resultado)}')
elif opcao_linha == 7:
    print(f'Em uma produção de {quantidade_producao} batelasas na linha Aves/suinos, o total para o Ganel Aves/Suinos é de {formata_br(resultado)}')  
elif opcao_linha == 8:
    print(f'Em uma produção de {quantidade_producao} bateladas na linha Pet/Peixes, o total para o Granel Pet/Peixes é de {formata_br(resultado)}')
elif opcao_linha == 9:
    print(f'Em uma produção de {quantidade_producao} bateladas na linha Pet/Peixes (ração de cães), o total de Pacotes a ser tirado é de {formata_br(resultado)}')                          
else:
    print('Batelada não reconhecida')
print() 