import random

class Summoner:
    def __init__(self, nome, mana, afinidade) -> None:
        self.__nome = nome
        self.__mana = mana
        self.__afinidade = afinidade

    def get_nome(self):
        return self.__nome

    def get_mana(self):
        return self.__mana

    def get_afinidade(self):
        return self.__afinidade

    def exibir_detalhes(self):
        return f"Summoner: {self.get_nome()}\nMana: {self.get_mana()}\nAfinidade: {self.get_afinidade()}"

    def perder_mana(self):
        self.__mana -= 1
        return self.__mana

class Summon(Summoner):
    def __init__(self, nome, mana, afinidade, dano, defesa, passiva) -> None:
        super().__init__(nome, mana, afinidade)
        self.__dano = dano
        self.__defesa = defesa
        self.__passiva = passiva

    def get_dano(self):
        return self.__dano
    
    def get_defesa(self):
        return self.__defesa

    def get_passiva(self):
        return self.__passiva

    def exibir_detalhes(self):
        detalhes = super().exibir_detalhes()
        detalhes = detalhes.replace("Summoner:", "Summon:")
        return f"{detalhes}\nAtk: {self.get_dano()}\nDefesa: {self.get_defesa()}\nPassiva: {self.get_passiva()}"

    def receber_ataque(self, dano):
        self.__defesa -= dano
        if self.__defesa <= 0:
            self.__defesa = 0

    def atacar(self, alvo):
        dano = self.__dano
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!")

class SummonCombate(Summon):
    def __init__(self, dano, defesa, passiva) -> None:
        super().__init__(dano, defesa, passiva)
        self.summona_em_campo = summona_em_campo
        self.summona_em_campo = summona_em_campo

class Jogo(): 
    # Classe orquestradora do jogo
    def __init__(self) -> None:
        self.SummonerA = Summoner(nome="Aeris, a Feiticeira do Vazio", mana=6, afinidade="Vazio")
        self.SummonerB = Summoner(nome="Drakar, o Senhor das Chamas", mana=6, afinidade="Fogo")
        self.SummonerC = Summoner(nome="Gaius, o Titâ de Pedra", mana=6, afinidade="Terra")
        self.SummonerD = Summoner(nome="Freyja, a Bruxa do Gelo", mana=6, afinidade="Gelo")

        self.SummonA = Summon(nome="Demônio Sombrio", mana=1, afinidade="Sombrio", dano=5, defesa=10, passiva=2)
        self.SummonB = Summon(nome="Fênix de Fogo", mana=1, afinidade="Fogo", dano=6, defesa=12, passiva=2)
        self.SummonC = Summon(nome="Guerreiro da Chama Negra", mana=1, afinidade="Fogo", dano=6, defesa=8, passiva=2)
        self.SummonD = Summon(nome="Besta do Vazio", mana=1, afinidade="Vazio", dano=7, defesa=12, passiva=2)
        self.SummonE = Summon(nome="Anjo Guardião", mana=1, afinidade="Luz", dano=4, defesa=15, passiva=2)
        self.SummonF = Summon(nome="Cavaleiro Espectral", mana=1, afinidade="Sombrio", dano=5, defesa=10, passiva=2)
        self.SummonG = Summon(nome="Elemental da Tempestade", mana=1, afinidade="Relâmpago", dano=6, defesa=10, passiva=2)
        self.SummonH = Summon(nome="Serpente Abissal", mana=1, afinidade="Água", dano=5, defesa=12, passiva=2)
        self.SummonI = Summon(nome="Golem de Pedra", mana=1, afinidade="Terra", dano=3, defesa=18, passiva=2)
        self.SummonJ = Summon(nome="Dragão de Gelo", mana=1, afinidade="Gelo", dano=6, defesa=14, passiva=2)
        self.SummonK = Summon(nome="Minotauro Rochoso", mana=1, afinidade="Terra", dano=6, defesa=15, passiva=2)
        self.SummonL = Summon(nome="Quimera de Chamas", mana=1, afinidade="Fogo", dano=7, defesa=12, passiva=2)
        self.SummonM = Summon(nome="Hidra de Cristal", mana=1, afinidade="Gelo", dano=5, defesa=14, passiva=2)
        self.SummonN = Summon(nome="Dragão Sombrio", mana=1, afinidade="Sombrio", dano=8, defesa=12, passiva=2)
        self.SummonO = Summon(nome="Titã do Relâmpago", mana=1, afinidade="Relâmpago", dano=7, defesa=10, passiva=2)
        self.SummonP = Summon(nome="Leviatã Abissal", mana=1, afinidade="Água", dano=7, defesa=14, passiva=2)
        self.SummonQ = Summon(nome="Mago Arcano", mana=1, afinidade="Luz", dano=4, defesa=12, passiva=2)
        self.SummonR = Summon(nome="Lobo Espectral", mana=1, afinidade="Vazio", dano=6, defesa=12, passiva=2)
        self.SummonS = Summon(nome="Guardião de Pedra", mana=1, afinidade="Terra", dano=5, defesa=16, passiva=2)
        self.SummonU = Summon(nome="Mestre das Marés", mana=1, afinidade="Água", dano=6, defesa=14, passiva=2)
    
    def iniciar_batalha(self):
        """Faz a gestão da batalha em turnos"""
        print("Jogadores, escolham os seus Summoners: ")
        print(f"1. {self.SummonerA.get_nome()}")
        print(f"2. {self.SummonerB.get_nome()}")
        print(f"3. {self.SummonerC.get_nome()}")
        print(f"4. {self.SummonerD.get_nome()}")

        try:
            primeira_escolha = int(input("\nPrimeiro Summoner: "))
            segunda_escolha = int(input("Segundo Summoner: "))
        except ValueError:
            print("Erro: Digite apenas números!")
            return

        # Mapeamento de números para Summoners
        summoners = {
            1: self.SummonerA,
            2: self.SummonerB,
            3: self.SummonerC,
            4: self.SummonerD
        }

        # Verificar se as escolhas são válidas e diferentes
        if primeira_escolha in summoners and segunda_escolha in summoners and primeira_escolha != segunda_escolha:
            primeiro_summoner = summoners[primeira_escolha]
            segundo_summoner = summoners[segunda_escolha]
            print(f"Summoners escolhidos: {primeiro_summoner.get_nome()} e {segundo_summoner.get_nome()}")
        else:
            print("Algo deu errado! Escolha dois Summoners diferentes usando números de 1 a 4.")
            exit("Reinicie o Jogo")

        input("Pressione enter para Iniciar!")

        #Mapeamento de números para Summons
        summons = {
            1: self.SummonA,
            2: self.SummonB,
            3: self.SummonC,
            4: self.SummonD,
            5: self.SummonE,
            6: self.SummonF,
            7: self.SummonG,
            8: self.SummonH,
            9: self.SummonI,
            10: self.SummonJ,
            11: self.SummonK,
            12: self.SummonL,
            13: self.SummonM,
            14: self.SummonN,
            15: self.SummonO,
            16: self.SummonP,
            17: self.SummonQ,
            18: self.SummonR,
            19: self.SummonS,
            20: self.SummonU,
        }

        deck_a = []
        deck_b = []
        print(type(summons))
        deck_a.extend(random.sample(list(summons.values()), 7))
        deck_b.extend(random.sample(list(summons.values()), 7))
      
        rodada = 1
       
        a = 1
        for a in range(2):
            if rodada % 2 != 0:
                print(f"\nRodada: {rodada}")
                rodada += 1
                print(f"\n{primeiro_summoner.exibir_detalhes()}")
                print("\nSua Mão:\n")
                for indice, summons in enumerate(deck_a):
                    print(f"{indice + 1}: {deck_a[indice].exibir_detalhes()}\n")

                escolha_summon = int(input("Escolha um Summon para o combate: "))
                summona_em_campo = deck_a[escolha_summon - 1]
                print(f"{primeiro_summoner.get_nome()} sumonou {summona_em_campo.get_nome()}!")
            elif rodada % 2 == 0:
                print(f"\nRodada: {rodada}")
                rodada += 1
                print(f"\n{segundo_summoner.exibir_detalhes()}")
                print("\nSua Mão:\n")
                for indice, summons in enumerate(deck_b):
                    print(f"{indice + 1}: {deck_b[indice].exibir_detalhes()}\n")

                escolha_summon = int(input("Escolha um Summon para o combate: "))
                summonb_em_campo = deck_b[escolha_summon - 1]
                print(f"{segundo_summoner.get_nome()} sumonou {summonb_em_campo.get_nome()}!")

        rodada = 1

        while primeiro_summoner.get_mana() >= 0 and segundo_summoner.get_mana() >= 0:
            if rodada % 2 != 0:
                rodada += 1
                print(f"\n{primeiro_summoner.exibir_detalhes()}")
                print(f"\n{summona_em_campo.exibir_detalhes()}")
                print("\nO que deseja fazer: ")
                print("\n1. Atacar")
                acao = int(input())
                if acao == 1:
                    summona_em_campo.atacar(summonb_em_campo)
                    if summonb_em_campo.get_defesa() <= 0:
                        print(f"\n{summonb_em_campo.get_nome()} foi derrotado!\n")
                        segundo_summoner.perder_mana()
                        print(f"\n{segundo_summoner.exibir_detalhes()}\n")
                        deck_b.remove(summonb_em_campo)
                        summonb_em_campo = None
                        segundo_summoner.perder_mana()
                        
                        if segundo_summoner.get_mana() > 0 and summonb_em_campo == None:
                            for indice, summons in enumerate(deck_b):
                                print(f"{indice + 1}: {deck_b[indice].exibir_detalhes()}\n")

                            escolha_summon = int(input("Escolha um Summon para o combate: "))
                            summonb_em_campo = deck_b[escolha_summon - 1]
                            print(f"{segundo_summoner.get_nome()} sumonou {summonb_em_campo.get_nome()}!")
            
            elif rodada % 2 == 0:
                rodada += 1
                print(f"\n{segundo_summoner.exibir_detalhes()}")
                print(f"\n{summonb_em_campo.exibir_detalhes()}")
                print("\nO que deseja fazer: ")
                print("\n1. Atacar")
                acao = int(input())
                if acao == 1:
                    summonb_em_campo.atacar(summona_em_campo)
                    if summona_em_campo.get_defesa() <= 0:
                        print(f"\n{summona_em_campo.get_nome()} foi derrotado!\n")
                        primeiro_summoner.perder_mana()
                        print(f"\n{primeiro_summoner.exibir_detalhes()}\n")
                        deck_a.remove(summona_em_campo)
                        summona_em_campo = None

                        if primeiro_summoner.get_mana() > 0:
                            for indice, summons in enumerate(deck_a):
                                print(f"{indice + 1}: {deck_a[indice].exibir_detalhes()}\n")

                            escolha_summon = int(input("Escolha um Summon para o combate: "))
                            summona_em_campo = deck_a[escolha_summon - 1]
                            print(f"{primeiro_summoner.get_nome()} sumonou {summona_em_campo.get_nome()}!") 
            
        if primeiro_summoner.get_mana() == 0:
            print(f"Parabéns {primeiro_summoner.get_nome()} Venceu a batalha!")
        else:
            print(f"Parabéns {segundo_summoner.get_nome()} Venceu a batalha!")
                
# Criar instancia do jogo e iniciar batalha

jogo = Jogo()
jogo.iniciar_batalha()