class Memento:
    def __init__(self, estado):
        self.estado = estado


class Editor:
    def __init__(self):
        self.conteudo = ""

    def escrever(self, texto):
        self.conteudo += texto

    def salvar(self):
        return Memento(self.conteudo) 

    def restaurar(self, memento):
        self.conteudo = memento.estado

    def mostrar(self):
        print(f"{self.conteudo}")


class Historico:
    def __init__(self):
        self.mementos = []

    def adicionar_memento(self, memento):
        self.mementos.append(memento)

    def obter_memento(self, indice):
        return self.mementos[indice]


editor = Editor()
historico = Historico()

editor.escrever("Olá ")
historico.adicionar_memento(editor.salvar())

editor.escrever("mundo")
historico.adicionar_memento(editor.salvar())

editor.mostrar()


editor.restaurar(historico.obter_memento(0))
editor.mostrar()