"""is Indentidade comparar a mesma posição na memoria  /   in de associação   verificar presente numa sequencia

Estrutura For 
"""

"""texto = input("Digite um Texto")
VOGAIS = "AEIOU"

for letra in texto:
        if letra.upper() in VOGAIS:
            print(letra, end="")
print() """

"""Range """     

"""for numero in range(0,10,2):
    print(numero, end=".")
    print(numero)"""
    
""" While"""  
 
# programa com while 
opcao = -1

while opcao != 0:
    opcao = int(input("-1 scanear, -2 Consultar , -3 Varredura , 0 - SAIR"))
    
    if opcao == 1:
        print("Scaneando")
    elif opcao ==2:
        print("Consutando")
    elif opcao == 3:
        print("Varrendo ") 
    else:
        print("Saindo....")   