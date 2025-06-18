from datetime import datetime

print("'''Bem-vindo(a) ao Banco PyTrust'''\n")

# --- Constantes ---
MULTA_PERCENTUAL = 0.02          # 2% de multa sobre o valor original
JUROS_DIARIO_PERCENTUAL = 0.00033  # 0.033% de juros ao dia sobre o valor original
LIMITE_VALOR_BOLETO = 100000.00  # Limite máximo para o valor do boleto

while True:  # Envolve o código inteiro para permitir repetição

    # 1. Validação do Valor do Boleto
    while True:
        try:
            valor_str = input("Digite o valor do boleto bancário: R$").replace(',', '.')
            valor_boleto = float(valor_str)
            if valor_boleto <= 0:
                print("\nERRO: O valor do boleto deve ser maior que zero. Tente novamente.\n")
            elif valor_boleto > LIMITE_VALOR_BOLETO:
                print(f"\nERRO: Valor muito alto. O limite é R$ {LIMITE_VALOR_BOLETO:,.2f}. Tente novamente.\n")
            else:
                break
        except ValueError:
            print("\nERRO: Entrada inválida. Por favor, digite um número.\n")

    # 2. Validação da Data de Vencimento com formatação automática
    while True:
        data_str = input("\nDigite a data de vencimento (use ddmmaaaa ou dd/mm/aaaa): ")
        try:
            if len(data_str) == 8 and data_str.isdigit():
                data_formatada = f"{data_str[0:2]}/{data_str[2:4]}/{data_str[4:8]}"
            else:
                data_formatada = data_str

            data_vencimento = datetime.strptime(data_formatada, "%d/%m/%Y")
            break
        except ValueError:
            print("\nERRO! Data inválida. Verifique se a data existe e use o formato ddmmaaaa ou dd/mm/aaaa.\n")

    # 3. Validação da Data de Pagamento com formatação automática
    while True:
        data_str = input("\nDigite a data de pagamento (use ddmmaaaa ou dd/mm/aaaa): ")
        try:
            if len(data_str) == 8 and data_str.isdigit():
                data_formatada = f"{data_str[0:2]}/{data_str[2:4]}/{data_str[4:8]}"
            else:
                data_formatada = data_str

            data_pagamento = datetime.strptime(data_formatada, "%d/%m/%Y")
            break
        except ValueError:
            print("\nERRO! Data inválida. Verifique se a data existe e use o formato ddmmaaaa ou dd/mm/aaaa.\n")

    # --- Verificação da ordem das datas ---
    if data_pagamento < data_vencimento:
        print("\nATENÇÃO: A data de pagamento é anterior à data de vencimento. Não haverá multas ou juros.\n")
        diferenca_dias_atraso = 0 # Não há atraso
    else:
        # Calcula a diferença em dias entre pagamento e vencimento
        diferenca_dias_atraso = (data_pagamento - data_vencimento).days

    multa_atraso = 0
    juros_atraso = 0

    if diferenca_dias_atraso > 0:
        multa_atraso = valor_boleto * MULTA_PERCENTUAL
        juros_atraso = valor_boleto * JUROS_DIARIO_PERCENTUAL * diferenca_dias_atraso

    valor_total = valor_boleto + juros_atraso + multa_atraso

    # Impressão do boleto formatado
    print("\n" + "="*45)
    print(f"{'BANCO PYTHON S/A':^45}")
    print("="*45)
    print(f"Data de Vencimento : {data_vencimento.strftime('%d/%m/%Y')}")
    print(f"Data de Pagamento  : {data_pagamento.strftime('%d/%m/%Y')}")
    print(f"Dias de Atraso     : {max(0, diferenca_dias_atraso)}") # Garante que não mostra dias negativos
    print("-" * 45)
    print(f"Valor Original     : R$ {valor_boleto:,.2f}")
    print(f"Multa ({MULTA_PERCENTUAL*100:.0f}%)           : R$ {multa_atraso:,.2f}") # Mostra a porcentagem da constante
    print(f"Juros ({JUROS_DIARIO_PERCENTUAL*100:.3f}%/dia): R$ {juros_atraso:,.2f}") # Mostra a porcentagem da constante
    print("-" * 45)
    print(f"{'VALOR TOTAL':<20}: R$ {valor_total:,.2f}")
    print("="*45)
    print(f"{'Este documento não tem valor fiscal.':^45}")
    print("="*45)

    # Opção de continuar ou sair
    opcao = input("\nQuer analisar outro boleto? (s/n): ").lower()
    if opcao != 's':
        print("\nObrigado por usar o Banco PyTrust! Até mais!\n")
        break
