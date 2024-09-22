# Crie um programa em Python que simule um sistema de login. O programa deve permitir ao usuário três tentativas para acertar o nome de usuário e a senha corretos. Caso o usuário erre as credenciais, o programa deve fornecer uma mensagem informando quantas tentativas restam. Se o usuário acertar, uma mensagem de boas-vindas deve ser exibida, e o programa deve terminar imediatamente.


# Se todas as três tentativas falharem, o programa deve usar um loop for para exibir uma mensagem de "Acesso bloqueado" repetida três vezes.

#Entrada do programa e variaveis usuario  e senha e maximo de tentativas:

usuario  = "admin"
senha = "1234"
maxim_tenta = 3

#Estrutura de repetiçao For  para realizar as tentativas de login


for tentativa in range(1,maxim_tenta + 1):
        usuario = input ("Digite o nome do usuario:") #Bloco onde solicita  o usuario

        senha =  input ("Digite a senha:") #bloco  onde solicita a senha

#estrutura de condicao if  para verificar se usuario e senha estao corretos dentro do bloco de repetiçao For

        if  usuario == "admin" and senha == "1234":
                print ("Seja Bem Vindo ao Programa")  #Mensagem de boas vindas

                break
        else:
                tentativa_restantes = maxim_tenta - tentativa
                print (f"Login ou senha incorretos. Tentativas restantes: {tentativa_restantes}")

                if tentativa_restantes == 0:  #estrutura de condicao para verificar se as tentativas acabaram

                        for  i in range(3):
                                print ("Usuario Bloqueado")

                  





    

