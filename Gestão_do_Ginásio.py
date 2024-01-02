import tkinter as tk
from tkinter import messagebox
import pandas as pd


class Pessoa:
    def __init__(self, nome_utilizador, senha, idade, peso, sexo, altura, role="user"):
        self.nome_utilizador = nome_utilizador
        self.senha = senha
        self.idade = idade
        self.peso = peso
        self.sexo = sexo
        self.altura = altura
        self.role = role


class Sala:
    def __init__(self, nome, lotacao):
        self.nome = nome
        self.lotacao = lotacao


class EventoouAula:
    def __init__(self, nome, dia, horas, sala, duracao, especial):
        self.nome = nome
        self.dia = dia
        self.horas = horas
        self.sala = sala
        self.duracao = duracao
        self.especial = especial


class Aplicacao:
    def __init__(self, janela):
        self.pessoa_logada = None
        self.janela = janela
        self.janela.title("Ginásio App")
        self.janela.geometry ('925x500+300+200')
        self.janela.configure(bg="#fff")
        self.janela.resizable (False, False)
    
       
        self.img= tk.PhotoImage (file='gym.png')
        self.imagem = tk.Label (self.janela, image=self.img, bg='white').place(x=50, y=50)

        self.frame_login = tk.Frame(self.janela, bg="#fff",width=350,height=350)
        self.frame_login.place(x=480, y=70) 
        
        self.label_utilizador = tk.Label(self.frame_login, text="Utilizador:",bg="#fff")
        self.label_utilizador.place(x=40, y=80)
        self.entry_utilizador = tk.Entry(self.frame_login,width=30)
        self.entry_utilizador.place(x=140, y=80)

        self.label_senha = tk.Label(self.frame_login, text="Senha:",bg="#fff")
        self.label_senha.place(x=40, y=120)
        self.entry_senha = tk.Entry(self.frame_login, show="*",width=30)
        self.entry_senha.place(x=140, y=120)

        self.botao_login = tk.Button(self.frame_login, width=39, pady=7, text='Login', bg='#cc8a18', fg='white', border=0, command=self.efetuar_login)
        self.botao_login.place(x=40, y=160)

        self.botao_criar_conta = tk.Button(self.frame_login, width=39, pady=7, text='Criar Conta', bg='#cc8a18', fg='white', border=0, command=self.mostrar_frame_conta)
        self.botao_criar_conta.place(x=40, y=200)

        self.frame_conta = tk.Frame(self.janela,bg="#fff",width=925,height=500)

        self.img= tk.PhotoImage (file='gym.png')
        self.imagem = tk.Label (self.janela, image=self.img, bg='white').place(x=50, y=50)

        self.label_nova_conta = tk.Label(self.frame_conta, text="Criar Nova Conta",bg="#fff")
        self.label_nova_conta.place(x=600, y=50)

        self.label_novo_utilizador = tk.Label(self.frame_conta, text="Novo Utilizador:",bg="#fff")
        self.label_novo_utilizador.place(x=470, y=100)
        self.entry_novo_utilizador = tk.Entry(self.frame_conta, width=31)
        self.entry_novo_utilizador.place(x=600, y=100)

        self.label_nova_senha = tk.Label(self.frame_conta, text="Nova Palavra-Passe:",bg="#fff")
        self.label_nova_senha.place(x=470, y=150)
        self.entry_nova_senha = tk.Entry(self.frame_conta, show="*", width=31)
        self.entry_nova_senha.place(x=600, y=150)

        self.label_idade = tk.Label(self.frame_conta, text="Idade:",bg="#fff")
        self.label_idade.place(x=470, y=200)
        self.entry_idade = tk.Entry(self.frame_conta, width=31)
        self.entry_idade.place(x=600, y=200)

        self.label_peso = tk.Label(self.frame_conta, text="Peso (KG):",bg="#fff")
        self.label_peso.place(x=470, y=250)
        self.entry_peso = tk.Entry(self.frame_conta, width=31)
        self.entry_peso.place(x=600, y=250)

        self.label_sexo = tk.Label(self.frame_conta, text="Sexo (M/F):",bg="#fff")
        self.label_sexo.place(x=470, y=300)
        self.entry_sexo = tk.Entry(self.frame_conta, width=31)
        self.entry_sexo.place(x=600, y=300)

        self.label_altura = tk.Label(self.frame_conta, text="Altura (CM):",bg="#fff")
        self.label_altura.place(x=470, y=350)
        self.entry_altura = tk.Entry(self.frame_conta, width=31)
        self.entry_altura.place(x=600, y=350)

        self.botao_criar_conta_final = tk.Button(self.frame_conta, text="Criar Conta", width=27, pady=7, bg='#cc8a18', fg='white', border=0,command=self.criar_conta)
        self.botao_criar_conta_final.place(x=600, y=380)

        self.frame_conta.pack(padx=50, pady=50)
        self.frame_conta.pack_forget()

        self.frame_pagina_principal = tk.Frame(self.janela,bg="#fff",width=350,height=350)

        self.botao_detalhes_pessoais = tk.Button(self.frame_pagina_principal,width=43, pady=7, bg='#e3a02b', fg='white', border=0 ,text="Ver Detalhes Pessoais",command=self.ver_detalhes_pessoais,)
        self.botao_detalhes_pessoais.place(x=20,y=0)

        self.botao_preco = tk.Button(self.frame_pagina_principal, text="Preços",width=43, pady=7, bg='#cf9125', fg='white', border=0 , command=self.mostrar_precos)
        self.botao_preco.place(x=20,y=50)

        self.botao_horario_semanal = tk.Button(
            self.frame_pagina_principal, text="Horário Semanal", width=43, pady=7, bg='#b8801f', fg='white', border=0 ,command=self.mostrar_horario_semanal)
        self.botao_horario_semanal.place(x=20,y=100)

        self.dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta","Sabado","Domingo"]
        self.indice_dia_atual = 0

        self.participaraula = tk.Button(self.frame_pagina_principal,text="Participar de uma Aula",width=43, pady=7, bg='#9e6e19', fg='white', border=0 ,command=self.mostrar_aulas_para_participar,)
        self.participaraula.place(x=20,y=150)

        self.botao_mostrar_aulas = tk.Button(self.frame_pagina_principal,text="Mostrar Aulas",width=43, pady=7, bg='#6e4b0e', fg='white', border=0 ,command=self.mostrar_aulas)
        self.botao_mostrar_aulas.place(x=20,y=250)

        self.frame_criar_aula_evento = tk.Frame(self.janela,bg="#fff",width=920,height=500)
        self.botao_criar_aula_evento = tk.Button(self.frame_pagina_principal,text="Criar Aula / Evento",width=43, pady=7, bg='#8a5f15', fg='white', border=0 ,command=self.criaraulaframe)
        self.botao_criar_aula_evento.place(x=20,y=200)

        self.botao_criar_aula_evento = tk.Button(self.frame_pagina_principal, text="Criar Aula / Evento", width=43, pady=7, bg='#8a5f15', fg='white', border=0, command=self.criaraulaframe)
        self.botao_criar_aula_evento.place(x=20, y=200)

        self.label_nome_aula_evento = tk.Label(self.frame_criar_aula_evento, text="Nome:",bg="#fff")
        self.label_nome_aula_evento.place(x=380, y=100) 
        self.entry_nome_aula_evento = tk.Entry(self.frame_criar_aula_evento,width=34)
        self.entry_nome_aula_evento.place(x=450, y=100)  

        self.label_dia_aula_evento = tk.Label(self.frame_criar_aula_evento, text="Dia:",bg="#fff")
        self.label_dia_aula_evento.place(x=380, y=150) 
        self.entry_dia_aula_evento = tk.Entry(self.frame_criar_aula_evento,width=34)
        self.entry_dia_aula_evento.place(x=450, y=150)  

        self.label_horas_aula_evento = tk.Label(self.frame_criar_aula_evento, text="Horas:",bg="#fff")
        self.label_horas_aula_evento.place(x=380, y=200)  
        self.entry_horas_aula_evento = tk.Entry(self.frame_criar_aula_evento,width=34)
        self.entry_horas_aula_evento.place(x=450, y=200)  

        self.label_sala_aula_evento = tk.Label(self.frame_criar_aula_evento, text="Sala:",bg="#fff")
        self.label_sala_aula_evento.place(x=380, y=250)  
        self.entry_sala_aula_evento = tk.Entry(self.frame_criar_aula_evento,width=34)
        self.entry_sala_aula_evento.place(x=450, y=250) 

        self.label_duracao_aula_evento = tk.Label(self.frame_criar_aula_evento, text="Duração:",bg="#fff")
        self.label_duracao_aula_evento.place(x=380, y=300) 
        self.entry_duracao_aula_evento = tk.Entry(self.frame_criar_aula_evento,width=34)
        self.entry_duracao_aula_evento.place(x=450, y=300) 

        self.label_especial_aula_evento = tk.Label(self.frame_criar_aula_evento, text="Especial:",bg="#fff")
        self.label_especial_aula_evento.place(x=380, y=350)  
        self.entry_especial_aula_evento = tk.Entry(self.frame_criar_aula_evento,width=34)
        self.entry_especial_aula_evento.place(x=450, y=350)  

        self.botao_submeter_aula = tk.Button(self.frame_criar_aula_evento, text="Submeter", width=41, pady=7, bg='#cc8a18', fg='white', border=0, command=self.CriarAulaEvento)
        self.botao_submeter_aula.place(x=380, y=400)

        self.botao_logout = tk.Button(self.frame_pagina_principal, text="Logout",width=43, pady=7, bg='#52370a', fg='white', border=0 , command=self.efetuar_logout)
        self.botao_logout.place(x=20,y=300)


    def mostrar_aulas_para_participar(self):
        try:
            df_aulas = pd.read_excel("dados_aulas.xlsx")

            if "Participantes" not in df_aulas.columns:
                df_aulas["Participantes"] = df_aulas.apply(lambda row: [], axis=1)

            if not df_aulas.empty:
                aulas_window = tk.Toplevel(self.janela)
                aulas_window.title("Aulas Disponíveis para Participar")

                def participar_aula(aula_nome):
                    if self.pessoa_logada:
                        participantes_list = df_aulas.loc[
                            df_aulas["Nome"] == aula_nome, "Participantes"
                        ].values[0]

                        if not isinstance(participantes_list, list):
                            participantes_list = []

                        if self.pessoa_logada.nome_utilizador not in participantes_list:
                            participantes_list.append(
                                self.pessoa_logada.nome_utilizador
                            )

                            df_aulas.loc[
                                df_aulas["Nome"] == aula_nome, "Participantes"
                            ] = [participantes_list]
                            df_aulas.to_excel("dados_aulas.xlsx", index=False)
                            messagebox.showinfo(
                                "Participação",
                                f"Você inscreveu-se na aula: {aula_nome}",
                            )
                        else:
                            messagebox.showinfo(
                                "Aviso", f"Você já está inscrito na aula: {aula_nome}"
                            )
                    else:
                        messagebox.showerror(
                            "Erro",
                            "Você precisa de fazer login para participar numa aula.",
                        )

                for index, row in df_aulas.iterrows():
                    aula_nome = row["Nome"]
                    button_text = f"Nome: {row['Nome']}, Dia: {row['Dia']}, Horas: {row['Horas']}, Sala: {row['Sala']}, Duração: {row['Duracao']}, Especial: {row['Especial']}"
                    aula_button = tk.Button(
                        aulas_window,
                        text=button_text,
                        command=lambda aula=aula_nome: participar_aula(aula),
                    )
                    aula_button.pack(pady=5)

            else:
                messagebox.showinfo("Aulas", "Nenhuma aula disponível para participar!")

        except FileNotFoundError:
            messagebox.showerror("Erro", "Nenhum arquivo de aulas encontrado!")


    def efetuar_login(self):
        utilizador = self.entry_utilizador.get()
        senha = self.entry_senha.get()

        if utilizador and senha:
            try:
                df = pd.read_excel("dados_utilizadors.xlsx")
                match = df[(df["Utilizador"] == utilizador) & (df["Senha"] == senha)]

                if not match.empty:
                    pessoa_data = match.iloc[0]
                    pessoa = Pessoa(
                        pessoa_data["Utilizador"],
                        pessoa_data["Senha"],
                        pessoa_data["Idade"],
                        pessoa_data["Peso"],
                        pessoa_data["Sexo"],
                        pessoa_data["Altura"],
                        pessoa_data.get("Role", "user"),
                    )

                    self.pessoa_logada = pessoa

                    if pessoa.role == "admin":
                        messagebox.showinfo(
                            "Login", "Admin login efetuado com sucesso!"
                        )
                    else:
                        messagebox.showinfo("Login", "Login efetuado com sucesso!")

                    self.frame_login.pack_forget()
                    self.frame_pagina_principal.place(x=480, y=70) 

                else:
                    messagebox.showerror("Erro", "Utilizador ou senha incorretos!")

            except FileNotFoundError:
                messagebox.showerror("Erro", "Nenhum Utilizador criado ainda!")
        else:
            messagebox.showerror("Erro", "Utilizador e senha são obrigatórios!")



    def mostrar_frame_login(self):
        self.frame_pagina_principal.pack_forget()
        self.frame_conta.pack_forget()
        self.frame_login.pack()
        self.frame_login.place(x=480, y=70)
        self.label_utilizador.pack()
        self.label_utilizador.place(x=40, y=80)
        self.entry_utilizador.pack()
        self.entry_utilizador.place(x=140, y=80)
        self.label_senha.pack()
        self.label_senha.place(x=40, y=120)
        self.entry_senha.pack()
        self.entry_senha.place(x=140, y=120)
        self.botao_login.pack()
        self.botao_login.place(x=40, y=160)
        self.botao_criar_conta.pack()
        self.botao_criar_conta.place(x=40, y=200)



    def criaraulaframe(self):
        if self.pessoa_logada and self.pessoa_logada.role == "admin":
            self.frame_criar_aula_evento.pack()
            self.frame_pagina_principal.pack_forget()
        else:
            messagebox.showerror("Erro", "Não é administrador")


    def efetuar_logout(self):
        self.pessoa_logada = None
        for widget in self.frame_pagina_principal.winfo_children():
            widget.destroy()
        self.frame_pagina_principal.pack()
        self.frame_pagina_principal.pack_forget()
        self.mostrar_frame_login()

        
    def mostrar_pagina_principal(self):
        self.frame_login.pack_forget()
        self.frame_conta.pack_forget()
        self.frame_criar_aula_evento.pack_forget()
        self.frame_pagina_principal.pack()
        self.frame_pagina_principal.place(x=480, y=70)
    

    def CriarAulaEvento(self):
        if self.pessoa_logada and self.pessoa_logada.role == "admin":
            self.frame_pagina_principal.pack_forget()

            nome_aula_evento = self.entry_nome_aula_evento.get()
            dia_aula_evento = self.entry_dia_aula_evento.get()
            horas_aula_evento = self.entry_horas_aula_evento.get()
            sala_aula_evento = self.entry_sala_aula_evento.get()
            duracao_aula_evento = self.entry_duracao_aula_evento.get()
            especial_aula_evento = self.entry_especial_aula_evento.get()

            if (
                nome_aula_evento
                and dia_aula_evento
                and horas_aula_evento
                and duracao_aula_evento
                and especial_aula_evento
            ):

                if self.SalaExistente(sala_aula_evento):

                    nova_aula_evento = EventoouAula(
                        nome_aula_evento,
                        dia_aula_evento,
                        horas_aula_evento,
                        sala_aula_evento,
                        duracao_aula_evento,
                        especial_aula_evento,
                    )

                    self.adicionar_dados_excelAula(nova_aula_evento)

                    self.entry_nome_aula_evento.delete(0, tk.END)
                    self.entry_dia_aula_evento.delete(0, tk.END)
                    self.entry_horas_aula_evento.delete(0, tk.END)
                    self.entry_sala_aula_evento.delete(0, tk.END)
                    self.entry_duracao_aula_evento.delete(0, tk.END)
                    self.entry_especial_aula_evento.delete(0, tk.END)

                    self.mostrar_pagina_principal()

                else:
                    messagebox.showerror("Erro", "A sala inserida não existe!")

            else:
                messagebox.showerror(
                    "Erro", "Todos os campos são obrigatórios para criar aula/evento."
                )
        else:
            messagebox.showerror(
                "Erro",
                "Você não tem permissão para criar aula/evento. Faça login como administrador.",
            )



    def SalaExistente(self, nome_sala):
        dados_sala = "dados_salas.xlsx"
        readdadossala = pd.read_excel(dados_sala)
        coluna_verificacao = "Nome"

        if nome_sala in readdadossala[coluna_verificacao].values:
            return True
        else:
            return False
        




    def mostrar_precos(self):
        precos = (
            "Mensalidade: 30€\n"
            "1 Aula: 10€\n"
            "1 hora de ginásio: 7,5€\n"
            "Personal Trainer + Mensalidade: 90€\n"
            "1 hora de piscina: 10€\n"
            "Consulta Nutrição: 35€"
        )
        messagebox.showinfo("Preços", precos)


    def mostrar_horario_semanal(self):
        self.horario_window = tk.Toplevel(self.janela)
        self.horario_window.title("Horário Semanal")

        self.frame_horario = tk.Frame(self.horario_window)
        self.frame_horario.pack()

        label_dia_semana = tk.Label(
            self.frame_horario, text=f"Horário para {self.dias_semana[self.indice_dia_atual]}"
        )
        label_dia_semana.pack(pady=10)


        botao_proximo_dia = tk.Button(
            self.frame_horario, text="Próximo Dia", command=self.proximo_dia
        )
        botao_proximo_dia.pack(pady=10)

        self.exibir_horario_dia()



    def proximo_dia(self):
        self.frame_horario.destroy()

        self.indice_dia_atual = (self.indice_dia_atual + 1) % len(self.dias_semana)

        self.frame_horario = tk.Frame(self.horario_window)
        self.frame_horario.pack()

        label_dia_semana = tk.Label(
            self.frame_horario, text=f"Horário para {self.dias_semana[self.indice_dia_atual]}"
        )
        label_dia_semana.pack(pady=10)

        botao_proximo_dia = tk.Button(
            self.frame_horario, text="Próximo Dia", command=self.proximo_dia
        )
        botao_proximo_dia.pack(pady=10)

        self.exibir_horario_dia()



    def exibir_horario_dia(self):
        try:
            df_horario = pd.read_excel("horario_semanal.xlsx")

            dia = self.dias_semana[self.indice_dia_atual]
            if dia in ["Sabado", "Domingo"]:
                mensagem_descanso = " Dia de descanso"
                label_folga = tk.Label(self.frame_horario, text=mensagem_descanso)
                label_folga.pack(pady=10)
            else:
                aulas_dia_atual = df_horario[df_horario["Dia"] == dia]

            for index, row in aulas_dia_atual.iterrows():
                info_aula = f"Nome: {row['Nome']}, Horas: {row['Horas']}, Sala: {row['Sala']}"
                label_aula = tk.Label(self.frame_horario, text=info_aula)
                label_aula.pack(pady=5)

        except FileNotFoundError:
            messagebox.showerror("Erro", "Arquivo 'horario_semanal.xlsx' não encontrado!")




    def ver_detalhes_pessoais(self):
        if self.pessoa_logada:
            detalhes = (
                f"Utilizador: {self.pessoa_logada.nome_utilizador}\n"
                f"Idade: {self.pessoa_logada.idade}\n"
                f"Peso: {self.pessoa_logada.peso}\n"
                f"Sexo: {self.pessoa_logada.sexo}\n"
                f"Altura: {self.pessoa_logada.altura}"
            )
            messagebox.showinfo("Detalhes Pessoais", detalhes)
        else:
            messagebox.showerror("Erro", "Nenhum Utilizador logado!")




    def mostrar_frame_conta(self):
        self.entry_utilizador.delete(0, tk.END)
        self.entry_senha.delete(0, tk.END)
        self.botao_criar_conta.pack_forget()
        
        if self.frame_login.winfo_ismapped():
            self.frame_login.pack_forget()
            self.frame_conta.pack()
        else:
            self.frame_conta.pack_forget()
            self.frame_login.pack()


    

    def criar_conta(self):
        novo_utilizador = self.entry_novo_utilizador.get()
        nova_senha = self.entry_nova_senha.get()
        idade = self.entry_idade.get()
        peso = self.entry_peso.get()
        sexo = self.entry_sexo.get()
        altura = self.entry_altura.get()

        if novo_utilizador and nova_senha and idade and peso and sexo and altura:
            
            if not idade.isdigit():
                messagebox.showinfo("Erro","A idade requerida situa-se entre 0 e 150 anos.")
                return

            if int(idade) <0 or int(idade) >150:
                messagebox.showinfo("Erro","A idade requerida situa-se entre 0 e 150 anos.")
                return
            
            if not peso.isdigit():
                messagebox.showinfo("Erro","O seu peso tem que ser um número acima de 0.")
                return

            if int(peso) <0:
                messagebox.showinfo("Erro","O seu peso tem que ser um número acima de 0.")
                return
            
            if sexo not in["F", "M"]:
                messagebox.showinfo("Erro","Sexo tem que ser M ou F.",)
                return
            
            if not altura.isdigit():
                messagebox.showinfo("Erro","A sua altura tem de se encontrar entre 0 e 300 centímetros.")
                return
            
            if int(altura) <0 or int(altura) >300:
                messagebox.showinfo("Erro","A sua altura tem de se encontrar entre 0 e 300 centímetros.")
                return
            
            nova_pessoa = Pessoa(novo_utilizador, nova_senha, idade, peso, sexo, altura, "user")
            messagebox.showinfo("Conta Criada",f"Nova conta criada com sucesso!\nUtilizador: {novo_utilizador}\nIdade: {idade}\nPeso: {peso}\nSexo: {sexo}\nAltura: {altura}\n",)

            self.adicionar_dados_excel(nova_pessoa)

            self.entry_novo_utilizador.delete(0, tk.END)
            self.entry_nova_senha.delete(0, tk.END)
            self.entry_idade.delete(0, tk.END)
            self.entry_peso.delete(0, tk.END)
            self.entry_sexo.delete(0, tk.END)
            self.entry_altura.delete(0, tk.END)

            self.mostrar_frame_login()
            
        else:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")



    def adicionar_dados_excel(self, pessoa):
        dados = {
            "Utilizador": [pessoa.nome_utilizador],
            "Senha": [pessoa.senha],
            "Idade": [pessoa.idade],
            "Peso": [pessoa.peso],
            "Sexo": [pessoa.sexo],
            "Altura": [pessoa.altura],
            "Role": [pessoa.role],
        }

        try:
            df_existente = pd.read_excel("dados_utilizadors.xlsx")

            df_novo = pd.DataFrame(dados)
            df_final = pd.concat([df_existente, df_novo], ignore_index=True)
        except FileNotFoundError:

            df_final = pd.DataFrame(dados)

        df_final.to_excel("dados_utilizadors.xlsx", index=False)



    def adicionar_dados_excelAula(self, aula):

        dados = {
            "Nome": [aula.nome],
            "Dia": [aula.dia],
            "Horas": [aula.horas],
            "Sala": [aula.sala],
            "Duracao": [aula.duracao],
            "Especial": [aula.especial],
        }

        try:
            df_existente = pd.read_excel("dados_aulas.xlsx")

            df_novo = pd.DataFrame(dados)
            df_final = pd.concat([df_existente, df_novo], ignore_index=True)
        except FileNotFoundError:

            df_final = pd.DataFrame(dados)

        df_final.to_excel("dados_aulas.xlsx", index=False)




    def mostrar_aulas(self):
        try:

            df_aulas = pd.read_excel("dados_aulas.xlsx")

            if not df_aulas.empty:
                aulas = "\n".join(
                    [
                        f"Nome: {row['Nome']}, Dia: {row['Dia']}, Horas: {row['Horas']}, Sala: {row['Sala']}, Duração: {row['Duracao']}, Especial: {row['Especial']}"
                        for index, row in df_aulas.iterrows()
                    ]
                )
                messagebox.showinfo("Aulas", aulas)
            else:
                messagebox.showinfo("Aulas", "Nenhuma aula criada!")

        except FileNotFoundError:
            messagebox.showerror("Erro", "Nenhum arquivo de aulas encontrado!")


if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacao(root)
    root.mainloop()
