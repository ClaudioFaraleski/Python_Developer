import time

nome = "Claudio"

menu = ("""
     =================== Sistema Bancario =======================
                          Seja bem vindo 
      (d) - depositar
      (s) - sacar
      (e) - extrato
      (q) - sair 
      
      """)



saldo = 0
saque = 0
deposito = 0
limite = 500
n_saques = 0
extrato = ""
LIMITE_SAQUE = 3


while True:
    
    menu = input(menu) 
    
    if menu == "d".lower():
        deposito = int(input("Qual valor deseja depositar :"))

        if deposito >0:
            saldo+=deposito
            print("Aguarde...")
            time.sleep(5)
            extrato += f"\nDesposito R${deposito:.2f}\n"
            print("Deposito realizado com sucesso")
        else:
            print("o valor não pode ser negativo, verifique e tente novamente")
            
      ##############################################################################      
    if menu == "s".lower():
        saque = int(input("Qual valor deseja sacar :"))


        excedeu_saldo =  saque > saldo

        excedeu_limite = saque > limite

        excedeu_saque = n_saques >= LIMITE_SAQUE


        if excedeu_saldo:
            print("Voce Não tem saldo Suficiente")
        elif excedeu_limite:
            print("Voce excedeu limite do dia")
        elif excedeu_saque:
            print("Numero de saques excedido")

        elif saque > 0:
            saldo -= saque
            extrato += f"Saque R$ {saque:.2f}\n"
            n_saques+=1

        else:
            print("Operação não realizada verifique e tente novamente")
    ##################################################################################################3
    if menu == "e".lower():

               print("\n================= extrato ====================")
               print("Não foram realizadas movimentações " if not extrato else extrato)
               print(f"\n Saldo : R$ {saldo:.2f}")


    
