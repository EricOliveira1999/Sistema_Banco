#menu_inicial
menu = ("""
        
[d] depósito       
[s] saque
[e] extrato
[q] sair
        
=> """)


saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)



#deposito
    if opcao == 'd':
        valor = float(input('informe o valor do depósito: '))

        if valor >0:
            saldo += valor
            extrato += f"depósito: R$ {valor:.2f}\n"

        else:
            print('operação falhou! o valor informado é inválido!')
   

#saque
    elif opcao == 's':
        valor = float(input('qual o valor você deseja sacar: '))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES


        if excedeu_saldo:
            print ('operação falhou! o seu saldo é insuficiente.')
        
        elif excedeu_limite:
            print ('operação falhou! o valor excedeu o limite da conta')

        elif excedeu_saques:
            print('operação falhou! número máximo de saques foi excedido')

        elif valor > 0:
            saldo -= valor
            extrato += f'saque: R${valor:.2f}\n'
            numero_saques += 1

        else: 
            print('operação falhou! o valor informado é inválido')


#extrato
    elif opcao == 'e':
        print ('\n=====================EXTRATO=========================')
        print('não foram realizadas movimentações.' if not extrato else extrato)
        print (f'\nSaldo: R${saldo:.2f}')
        print ('======================================================')
        


#sair
    elif opcao == 'q':
        print('obrigado por utilizar nosso sistema')
        break


#opcao invalida
    else:
        print('operação invalida, por favor selecione novamente a operação desejada')