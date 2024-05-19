
class ControladorEquipe:
    def __init__(self):
        self.equipes = []
        self.tela_equipe = TelaEquipe()

    def inclui_equipe(self):
        nome = self.tela_equipe.solicita_equipe()
        equipe = Equipe(nome)
        self.equipes.append(equipe)
        self.tela_equipe.mostrar_mensagem("Equipe adicionada com sucesso!")

    def inclui_pontos(self):
        nome_equipe = self.tela_equipe.solicita_equipe()
        equipe = self.pega_equipe_por_nome(nome_equipe)
        if equipe:
            pontos = int(input("Digite o número de pontos a adicionar: "))
            equipe.set_num_pontos(equipe.get_num_pontos() + pontos)
            self.tela_equipe.mostrar_pontos_equipe(equipe)
        else:
            self.tela_equipe.mostrar_mensagem("Equipe não encontrada!")

    def altera_dados_equipe(self):
        nome_equipe = self.tela_equipe.solicita_equipe()
        equipe = self.pega_equipe_por_nome(nome_equipe)
        if equipe:
            novo_nome = input("Digite o novo nome da equipe: ")
            equipe.set_nome(novo_nome)
            self.tela_equipe.mostrar_mensagem("Dados da equipe alterados com sucesso!")
        else:
            self.tela_equipe.mostrar_mensagem("Equipe não encontrada!")

    def exclui_equipe(self):
        nome_equipe = self.tela_equipe.solicita_equipe()
        equipe = self.pega_equipe_por_nome(nome_equipe)
        if equipe:
            self.equipes.remove(equipe)
            self.tela_equipe.mostrar_mensagem("Equipe removida com sucesso!")
        else:
            self.tela_equipe.mostrar_mensagem("Equipe não encontrada!")

    def pega_equipe_por_nome(self, nome):
        for equipe in self.equipes:
            if equipe.get_nome() == nome:
                return equipe
        return None

    def listar_equipes(self):
        if self.equipes:
            for equipe in self.equipes:
                self.tela_equipe.mostra_dados_equipe(equipe)
        else:
            self.tela_equipe.mostrar_mensagem("Nenhuma equipe cadastrada!")

    def abre_tela_equipe(self):
        while True:
            opcao = self.tela_equipe.tela_opcoes_equipe()
            if opcao == 1:
                self.listar_equipes()
            elif opcao == 2:
                self.inclui_equipe()
            elif opcao == 3:
                self.exclui_equipe()
            elif opcao == 4:
                self.altera_dados_equipe()
            elif opcao == 5:
                self.adicionar_aluno_equipe()
            elif opcao == 6:
                self.remover_aluno_equipe()
            elif opcao == 7:
                return
            else:
                print("Opção inválida!")

    def equipe_mais_gols(self):
        # lógica para encontrar a equipe com mais gols
        equipe_mais_gols = None
        return equipe_mais_gols

    def equipe_levou_mais_gols(self):
        #  para encontrar a equipe que levou mais gols
        pass

    def equipe_menos_gols(self):
        #para encontrar a equipe com menos gols
        pass 

    def adicionar_aluno_equipe(self):
        nome_equipe = self.tela_equipe.solicita_equipe()
        equipe = self.pega_equipe_por_nome(nome_equipe)
        if equipe:
            nome_aluno = input("Digite o nome do aluno: ")
            aluno = Aluno(nome_aluno, None, None, None)
            equipe.get_alunos().append(aluno)
            self.tela_equipe.mostrar_mensagem("Aluno adicionado à equipe!")
        else:
            self.tela_equipe.mostrar_mensagem("Equipe não encontrada!")

    def remover_aluno_equipe(self):
        nome_equipe = self.tela_equipe.solicita_equipe()
        equipe = self.pega_equipe_por_nome(nome_equipe)
        if equipe:
            nome_aluno = input("Digite o nome do aluno a ser removido: ")
            for i, aluno in enumerate(equipe.get_alunos()):
                if aluno.nome == nome_aluno:
                    del equipe.get_alunos()[i]
                    self.tela_equipe.mostrar_mensagem("Aluno removido da equipe!")
                    return
            self.tela_equipe.mostrar_mensagem("Aluno não encontrado na equipe!")
        else:
            self.tela_equipe.mostrar_mensagem("Equipe não encontrada!")