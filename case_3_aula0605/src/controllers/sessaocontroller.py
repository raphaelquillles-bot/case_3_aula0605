# src/controllers/sessaocontroller.py

class SessaoController:
    def __init__(self, service):
        self.service = service

    def adicionar_publico(self, id_sessao, qtd_publico):
        # O Controller chama o Service e devolve a resposta para a View
        sucesso, mensagem = self.service.registrar_publico(id_sessao, qtd_publico)
        return sucesso, mensagem