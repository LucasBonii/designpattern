from abc import ABC, abstractmethod


class Aluno(ABC):
    @abstractmethod
    def acessar_dados(self) -> None:
        pass


class RealAluno(Aluno):
    def __init__(self, nome: str, notas: list):
        self._nome = nome
        self._notas = notas

    def acessar_dados(self) -> None:
        print(f"Nome: {self._nome}")
        print(f"Notas: {self._notas}")


class ProxyAluno(Aluno):
    def __init__(self, real_aluno: RealAluno, autorizado: bool) -> None:
        self._real_aluno = real_aluno
        self._autorizado = autorizado

    def acessar_dados(self) -> None:
        if self.verificar_acesso():
            self._real_aluno.acessar_dados()
        else:
            print("Acesso negado!")

    def verificar_acesso(self) -> bool:
        return self._autorizado


def cliente(aluno: Aluno) -> None:
    aluno.acessar_dados()


aluno_real = RealAluno("Lucas Boni", [8.5, 7.0, 9.2])


proxy_sem_acesso = ProxyAluno(aluno_real, autorizado=False)
cliente(proxy_sem_acesso)



# Tentando acessar com autorização
proxy_com_acesso = ProxyAluno(aluno_real, autorizado=True)
cliente(proxy_com_acesso)
