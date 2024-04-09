print('**************Banco em Python**************')

senha_correta = "senha123"
tentativas = 0

while tentativas < 3:
        senha = input("Digite a senha: ")
        
        if senha == senha_correta:
            print("Senha correta. Acesso concedido!")
            # Coloque aqui o código que deseja executar após a senha correta
            break
        else:
            tentativas += 1
            if tentativas < 3:
                print("Senha incorreta. Tente novamente.")
    
if tentativas == 3:
        print("Você excedeu o número máximo de tentativas. Encerrando o programa.")


