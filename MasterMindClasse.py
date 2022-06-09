
import random

jogo=['X','X','X','X']
combinação=[]
senha=[]
derrota=10
class MasterMind:
    def __init__(self,jogo,combinaçao,senha):
        self.jogo=jogo
        self.combinaçao=combinaçao
        self.senha=senha
    def MostrarJogo(self):
        print(f"{self.jogo[0]} | {self.jogo[1]} | {self.jogo[2]} | {self.jogo[3]}")
        print(senha)
    
    def NumeroAleatorio(self):
        for c in range(0,4):
            numeroaleatorio=random.randint(0,9)
            senha.append(numeroaleatorio)
    
    def input(self):
        for c in range(0,4):
            ask=input("Digito: ")
            combinação.append(ask)

    def Verificar(self):
        if self.combinaçao == self.senha:
            print("Você é o mastermind!")
            for c in range(0,4):
                self.jogo[c] = senha[c]
                self.MostrarJogo()
            return True

        if self.combinaçao == self.senha and derrota == 10:
            print("Você acertou de primeira! Você é o MasterMind!")
            self.MostrarJogo()
            return True
        
        for elemento in range(0,4):
            if self.combinaçao[elemento] == self.senha[elemento]:
                jogo[elemento] = senha[elemento]
                self.MostrarJogo()
    def MensagemDeErroeErro(self):
        if self.combinaçao != self.senha:
            print("Esta não é a sequência!")
            print(f"Tentativas Restantes : {derrota}")
            return True

#Coloco a classe na variavel game
game=MasterMind(jogo,combinação,senha)

#Randomizo a lista de numero (Senha)

game.NumeroAleatorio()

#Programa Rodando
while True:
    game.MostrarJogo()
    game.input()
    if game.Verificar():
        break
    if game.MensagemDeErroeErro():
        derrota-=1
        if derrota == 0:
            print('Você perdeu!')
            break
