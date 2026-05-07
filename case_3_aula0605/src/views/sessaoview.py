# src/views/sessaoview.py

class SessaoView:
    def __init__(self, controller):
        self.controller = controller

    def exibir_menu_registro(self):
        print("\n--- 🎬 SISTEMA DO CINEMA: REGISTRAR PÚBLICO ---")
        try:
            id_sessao = int(input("Digite o ID da Sessão (Ex: 1): "))
            qtd_publico = int(input("Digite a quantidade de novos espectadores: "))
            
            sucesso, mensagem = self.controller.adicionar_publico(id_sessao, qtd_publico)
            
            if sucesso:
                print(f"✅ {mensagem}")
            else:
                print(f"❌ ERRO: {mensagem}")
        except ValueError:
            print("❌ ERRO: Por favor, digite apenas números inteiros válidos.")