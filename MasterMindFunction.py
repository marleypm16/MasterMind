import random
combinação=[]
senha=[]
jogo=['X','X','X','X']
derrota=10
def MostrarJogo(jogo):
    #Mostrar o Tabuleiro
    print(f'{jogo[0]} | {jogo[1]} | {jogo[2]} | {jogo[3]} ')
    print(f"{senha}")

def NumeroAleatorio():
    #Randomizar o número
    for c in range(0,4):
        numbersorted=random.randint(1,9)
        senha.append(numbersorted)

def Input():
    #Pergunto ao usuário o digito que ele vai escolher e adiciona na lista da combinação
    for c in range(0,4):
        ask=int(input('Digito:'))
        combinação.append(ask)
def Verificar(combinaçao,senha,jogo):
    #Verificar se a combinaçao escolhida pelo jogador é a correta
    if combinaçao == senha:
        print('Parabéns você acertou a sequência! Você é o MasterMind')
        for rang in range(0,4):
            jogo[rang] = senha[rang]
        MostrarJogo(jogo)
        return False
    if combinaçao == senha and derrota == 10:
        print("Você acertou de primeira, VOCÊ É O MASTERMIND diferenciado")
        return False

    for elemento in range(0,4):
        if combinaçao[elemento] == senha[elemento]:
            jogo[elemento] = senha[elemento]
            print("Número colocado na posição correta!")

                

def MensagemDeSequenciaIncorretaeDerrota(combinaçao,senha):
    #Verificar se a sequencia é diferente e caso as tentativas chegue a 0 o jogador perde
    if combinaçao != senha:
        print("-"*30)
        print("Esta não é a sequência correta")
        print(f"Tentativas restantes {derrota}")
        return True
            
       
print("-"*35)

print("MasterMind!")

print("O numero de 4 digitos ja foi sorteado! Boa Sorte")

print("-"*35)

#Ativar Funções


NumeroAleatorio()
while True:
    MostrarJogo(jogo)
    Input()
    if Verificar(combinação,senha,jogo) == False:
        break
    if MensagemDeSequenciaIncorretaeDerrota(combinação,senha):
        derrota-=1
        if derrota == 0:
            print("Você perdeu!")
            MostrarJogo(jogo)
            break