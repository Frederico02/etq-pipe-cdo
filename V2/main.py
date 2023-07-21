import tkinter as tk
import os

from impressora import Impressora
from dataHora import dia, hora


# Cria uma Classe da janela Principal
class TelaPrincipal:
    def __init__(self, janela):
        self.janela = janela
        janela.geometry("330x450")
        janela.title("Gerador de Etiquetas T.I")

        # Cria um frame para agrupar os widgets relacionados a "Insira o Código (CDO/PIPE)"
        frame_codigo = tk.Frame(self.janela)
        frame_codigo.grid(row=0, column=0, padx=10, pady=(10, 5))

        label_codigo = tk.Label(frame_codigo, text="Insira o Código (CDO/PIPE):    ")
        label_codigo.pack(side=tk.LEFT)

        self.codigo_JIRA = tk.StringVar()
        codigo_JIRA = tk.Entry(frame_codigo, textvariable=self.codigo_JIRA)
        codigo_JIRA.pack(side=tk.LEFT)

        # Cria um frame para agrupar os widgets relacionados a "Insira o Nome do colaborador"
        frame_nome = tk.Frame(self.janela)
        frame_nome.grid(row=1, column=0, padx=10, pady=5)

        label_nome = tk.Label(frame_nome, text="Insira o Nome do colaborador:")
        label_nome.pack(side=tk.LEFT)

        self.nome_colaborador = tk.StringVar()
        nome_colaborador = tk.Entry(frame_nome, textvariable=self.nome_colaborador)
        nome_colaborador.pack(side=tk.LEFT)

        # Cria um frame para agrupar os widgets relacionados a "Insira o QRCODE"
        frame_qr = tk.Frame(self.janela)
        frame_qr.grid(row=2, column=0, padx=10, pady=5)

        label_qr = tk.Label(frame_qr, text="Insira o QRCODE:                        ")
        label_qr.pack(side=tk.LEFT)

        self.qr = tk.StringVar()
        qr = tk.Entry(frame_qr, textvariable=self.qr)
        qr.pack(side=tk.LEFT)

        # Cria um frame para agrupar os widgets relacionados a "Insira o Ativo"
        frame_ativo = tk.Frame(self.janela)
        frame_ativo.grid(row=3, column=0, padx=10, pady=5)

        label_ativo = tk.Label(frame_ativo, text="Insira o Ativo:                              ")
        label_ativo.pack(side=tk.LEFT)

        self.ativo = tk.StringVar()
        ativo = tk.Entry(frame_ativo, textvariable=self.ativo)
        ativo.pack(side=tk.LEFT)

        # Criação dos outros widgets
        label_escolha = tk.Label(self.janela, text="Escolha uma Etiqueta:")
        label_escolha.grid(row=4, column=0, padx=10, pady=5)

        etq = ['','PIPE', 'CHAMADO']
        self.opcoes_etq = tk.StringVar(self.janela)
        self.opcoes_etq.set(etq[0])
        option_menu_etq = tk.OptionMenu(self.janela, self.opcoes_etq, *etq)
        option_menu_etq.grid(row=5, column=0, padx=10, pady=5)

        label_analista = tk.Label(self.janela, text="Analista:")
        label_analista.grid(row=6, column=0, padx=10, pady=5)

        nomes = ['','Arthur', 'Felipe', 'Fred', 'Jhones', 'Ralf', 'Thomas',]
        self.opcoes_nomes = tk.StringVar(self.janela)
        self.opcoes_nomes.set(nomes[0])
        option_menu_nomes = tk.OptionMenu(self.janela, self.opcoes_nomes, *nomes)
        option_menu_nomes.grid(row=7, column=0, padx=10, pady=5)

        self.btn_gerar = tk.Button(self.janela, text='Gerar Etiqueta', command=self.gerar, width=20)
        self.btn_gerar.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

        btn_sair = tk.Button(self.janela, text='Encerrar', command=self.encerrar, width=20)
        btn_sair.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

        label_dev = tk.Label(self.janela, text="© 2023 - MULTITECH. Todos os direitos reservados.")
        label_dev.grid(row=14, column=0, padx=10, pady=5)

    def gerar(self):
        codigo_JIRA = self.codigo_JIRA.get()
        nome_colaborador = self.nome_colaborador.get()
        qr = self.qr.get()
        ativo = self.ativo.get()
        dia_var = dia()
        hora_atual = hora()
        escolha_etiqueta = self.opcoes_etq.get()
        escolha_nome = self.opcoes_nomes.get()
        Impressora(dia_var, hora_atual, codigo_JIRA, nome_colaborador, qr, ativo, escolha_etiqueta, escolha_nome)

    def encerrar(self):
        janela_principal.destroy()



# Cria uma janela Principal
janela_principal = tk.Tk()
icone_path = 'm.ico'
janela_principal.iconbitmap(icone_path)
tela_principal = TelaPrincipal(janela_principal)
janela_principal.mainloop()
