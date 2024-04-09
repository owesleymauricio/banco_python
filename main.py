print('**************Banco em Python**************')

senha_correta = "senha123"
tentativas = 0

menu = """
[1] = saldo
[2] = saque
[3] = deposito
[4] = sair
"""
saldo = 500

while tentativas < 3:
    senha = input("Digite a senha: ")

    if senha != senha_correta:
         tentativas += 1
         if tentativas < 3:
           print("Senha incorreta. Tente novamente.")
         elif tentativas == 3:
             print("Você excedeu o número máximo de tentativas. Encerrando o programa.")
    else:
        print("Senha correta. Acesso concedido!")
        
        while True:
            opcao = input(menu)

            if opcao == '1':
                print('Você tem R${:.2f} reais'.format(saldo))
                print('================================')
                print('Deseja fazer outra transação?')

            elif opcao == '2':
                dinheiro_sacado_input = input('Quanto deseja sacar?\nR$')

                if dinheiro_sacado_input.isdigit() or dinheiro_sacado_input.replace('.', '', 1).isdigit():
                    dinheiro_sacado = float(dinheiro_sacado_input)

                    if dinheiro_sacado > saldo:
                        print('Você não possui esse saldo!')
                    else:
                        saldo -= dinheiro_sacado
                        print('Você sacou R${:.2f} reais'.format(dinheiro_sacado))
                        print('Seu saldo atual é de R${:.2f} reais.'.format(saldo))
                else:
                    print('Valor inválido! Tente novamente!')
                print('================================')
                print('Deseja fazer outra transação?')

            elif opcao == '3':
                dinheiro_depositado_input = input('Quanto deseja depositar?\nR$')

                if dinheiro_depositado_input.isdigit() or dinheiro_depositado_input.replace('.', '', 1).isdigit():
                    dinheiro_depositado = float(dinheiro_depositado_input)
                    saldo += dinheiro_depositado
                    print('Você depositou R${:.2f} reais'.format(dinheiro_depositado))
                    print('================================')
                else:
                    print('Valor inválido! Tente novamente!')
                    print('================================')
                print('Deseja fazer outra transação?')

            elif opcao == '4':
                print("Encerrando o programa...")
                break
        break    

print('Obrigado por usar nosso banco')
    
