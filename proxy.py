from abc import ABC, abstractmethod


class Aluno(ABC):
    @abstractmethod
    def acessar_dados(self):
        pass


class RealAluno(Aluno):
    def __init__(self, nome, notas):
        self._nome = nome
        self._notas = notas

    def acessar_dados(self):
        print(f"Nome: {self._nome}")
        print(f"Notas: {self._notas}")


class ProxyAluno(Aluno):
    def __init__(self, real_aluno, autorizado):
        self._real_aluno = real_aluno
        self._autorizado = autorizado

    def acessar_dados(self):
        if self.verificar_acesso():
            self._real_aluno.acessar_dados()
        else:
            print("Acesso negado!")

    def verificar_acesso(self):
        return self._autorizado


#def cliente(aluno):
#    aluno.acessar_dados()


aluno_real = RealAluno("Lucas Boni", [8.5, 7.0, 9.2])


proxy_sem_acesso = ProxyAluno(aluno_real, autorizado=False)
proxy_sem_acesso.acessar_dados()


proxy_com_acesso = ProxyAluno(aluno_real, autorizado=True)
proxy_com_acesso.acessar_dados()
