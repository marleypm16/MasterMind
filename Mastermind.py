#Mastermind
#Preciso Sortear um numero certo
#printo o jogo
#Preciso perguntar ao usuario pra vê se ele acerta o numero certo
#se ele acertar de primeira ai printo o numero normal
#se ele nao acertar quero que fosse mostrando de pouco em pouco por exemplo xxxx - xxx1 - xx31 - x231 - 4231 venceu

import random

senha=[]
print("-"*35)
print("Bem vindo ao MasterMind")
print("Numero de 4 digitos Sorteado! Tente Advinhar!")
print("-"*35)
jogo=['X','X','X','X']
for o in range(0,4):
    sortednumber=random.randint(1,9)
    senha.append(sortednumber)
combinaçao=[]
derrota=10
while True:
    for i in range(0,4):
        playerguess=int(input('Digito:'))
        combinaçao.append(playerguess)
    if  combinaçao == senha:
        print('Você é o mastermond')
        for elemento in range(0,4):
            jogo[elemento] = senha[elemento]
            print(jogo)
            break
    else:
        print(senha)
        for c in range (0,4):
            if combinaçao[c] == senha[c]:
                    print("há um numero na posição correta na sua sequencia")
                    jogo[c]=senha[c]
            print(jogo)
        if combinaçao != senha:
            derrota-=1
            print(f"esta nao é a sequencia correta! tentativas restantes {derrota}")
            combinaçao.clear()
            if derrota == 0:
                print("Você Perdeu")
                break
                
            
        
    


    
