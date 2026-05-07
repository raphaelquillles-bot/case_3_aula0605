# src/services/sessaoservice.py

class SessaoService:
    def __init__(self, repository):
        self.repository = repository

    def registrar_publico(self, id_sessao, qtd_publico):
        sessao = self.repository.buscar_por_id(id_sessao)
        
        if not sessao:
            return False, "Sessão não encontrada."
            
        capacidade_maxima = self.repository.buscar_capacidade_cinema_da_sessao(id_sessao)
        novo_total = sessao.publico_registrado + qtd_publico
        
        # Regra de Negócio: Validar Capacidade Máxima
        if novo_total > capacidade_maxima:
            return False, f"Capacidade excedida! A sala suporta {capacidade_maxima} pessoas. Já há {sessao.publico_registrado} registrados."
            
        # Salva no banco se passar na validação
        self.repository.atualizar_publico(id_sessao, novo_total)
        return True, f"Sucesso! Público atualizado para {novo_total} pessoas."