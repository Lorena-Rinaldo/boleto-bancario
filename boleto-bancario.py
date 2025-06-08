# Simulador de Boleto Bancário - Proposta 1

# Este programa solicita ao usuário:
# - Valor do boleto
# - Data de vencimento
# - Data de pagamento
# Ele calcula:
# - Dias de atraso (se houver)
# - Multa de 2% sobre o valor original
# - Juros de 0,033% ao dia de atraso
# - Valor total atualizado para pagamento

# Autores: Lívia Domingues Matos, Lorena Rinaldo Moreira, Lucas Assis Andrela e Luis Felipe de Lima Barros

import os
import platform
from datetime import datetime

while True:
    # Limpa o terminal dependendo do sistema operacional
    if platform.system() == "Windows": 
        os.system('cls') # Comando para Windows
    else:
        os.system('clear') # Comando para Linux/Mac

    print("'''Bem-vindo(a) ao Banco PyTrust'''\n")

    # Solicita ao usuário o valor do boleto (float para aceitar casas decimais)
    valor_boleto = float(input("Digite o valor do boleto bancário: R$"))

    # Solicita as datas de vencimento e pagamento no formato dd/mm/aaaa
    data_vencimento = input("\nDigite a data do vencimento do boleto (dd/mm/aaaa - não esqueça das barras): ")
    data_pagamento = input("\nDigite a data do pagamento do boleto (dd/mm/aaaa - não esqueça das barras): ")

    # Converte as strings das datas para objetos datetime para facilitar cálculos
    data_vencimento = datetime.strptime(data_vencimento, "%d/%m/%Y")
    data_pagamento = datetime.strptime(data_pagamento, "%d/%m/%Y")

    # Calcula a diferença em dias entre pagamento e vencimento
    diferenca_dias_atraso = (data_pagamento - data_vencimento).days

    # Inicializa multas e juros com zero para o caso de pagamento em dia
    multa_atraso = 0
    juros_atraso = 0

    # Caso haja atraso (diferença positiva), calcula multa e juros
    if diferenca_dias_atraso > 0:
        multa_atraso = valor_boleto * 0.02  # Multa fixa de 2% do valor original
        juros_atraso = valor_boleto * 0.00033 * diferenca_dias_atraso # Juros de 0,033% ao dia de atraso
        
    # Calcula o valor total a pagar (original + multa + juros)
    valor_total = valor_boleto + juros_atraso + multa_atraso

    # Impressão do boleto formatado, simulando um documento bancário
    print("\n" + "="*45)
    print(f"{'BANCO PYTHON S/A':^45}") # Nome do banco centralizado
    print("="*45)
    print(f"Data de Vencimento : {data_vencimento.strftime('%d/%m/%Y')}") # Data de vencimento formatada
    print(f"Data de Pagamento  : {data_pagamento.strftime('%d/%m/%Y')}")  # Data de pagamento formatada
    print(f"Dias de Atraso     : {max(diferenca_dias_atraso, 0)}") # Mostra 0 se não houver atraso
    print("-" * 45)
    print(f"Valor Original     : R$ {valor_boleto:,.2f}")  # Valor original com 2 casas decimais
    print(f"Multa (2%)         : R$ {multa_atraso:,.2f}") # Multa calculada
    print(f"Juros (0.033%/dia) : R$ {juros_atraso:,.2f}") # Juros calculados
    print("-" * 45)
    print(f"{'VALOR TOTAL':<20}: R$ {valor_total:,.2f}") # Valor total atualizado
    print("="*45)
    print(f"{'Este documento não tem valor fiscal.':^45}") # Mensagem de aviso centralizada
    print("="*45)

    opcao = input("\nQuer analisar outro boleto? (s/n): ").lower()

    if opcao != 's': #Se a opção for diferente de 's', aparecerá o print e encerrará o programa
        print("\nObrigado por usar o Banco PyTrust! Até mais!\n")
        break

    # Limpa a tela antes da próxima rodada
    if platform.system() == "Windows": 
        os.system('cls')
    else:
        os.system('clear')