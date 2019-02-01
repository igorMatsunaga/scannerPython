import socket # importando o módulo 

ip = input("Digite o IP da vitima: ") # entrada para IP
#ip = "216.58.202.174" # IP do google
portas = [11,10,21,22,25,3022,80,8080,8090,9043,443,8043,8443,9443,110,985,9080,9090] # lista de portas a serem scaneadas


for porta in portas:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET (representa o tipo de endereço), SOCK_STREAM (indica que socket é do tipo TCP)
    cliente.settimeout(2) # limite de tempo suportado
    conexao = cliente.connect_ex((ip, porta)) 
    
  # condição (se conexão for igual a 0 porta aberta se não porta fechada)
    with open("C:\\Users\\igortomio\\Desktop\\teste.txt", 'a') as f: # inserir caminho onde será salvo o arquivo
        if conexao == 0:
            f.write(str(porta)  + " >> porta aberta")
            f.writelines('\n')
            #print(porta)
        else:
            f.write(str(porta)  + " >> porta fechada") 
            f.writelines('\n')
           # print(porta)
            

    f.close() 
