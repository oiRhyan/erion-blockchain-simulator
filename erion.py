import customtkinter as ctk  # Biblioteca TKINTER baseada em BOOSTRAP
import json  # Biblioteca de Sistema JSON e Implementador
import datetime  # Controle de Data e Horario do Sistema em Tempo Real
import hashlib  # Biblioteca de Criptografia SHA
import time  # Biblioteca Time para Controle de Terminal
from PIL import Image  # Formatador de Imagem PNG
import pandas as pd  # Formatador para CSV Excel


# Diretorio do JSON e Tabela da BlockChain
bg_dados = 'bg_dados'
block_chain = []

# Relogio AO VIVO
hora_syntaxe = datetime.datetime.now().time()
hora_convertida = hora_syntaxe.strftime("%H:%M:%S")

# Intervalo de Tempo

# Conversor para Tabela EXCEL


def ConverterEXCEL():
    df = pd.read_json('bg_dados')
    df.to_csv('bg_dados.csv')


def get_time():
    return time.time()

# Validador de Dificuldade Segunda etapa


def isValidHashDifficulty(hash, difficulty):
    count = 0
    for i in hash:
        count += 1
        if (i != '0'):
            break
    return count >= difficulty

# Gerador de Hash e Validador de Segurança


def generate_hash(block):
    nonce = 0
    block["Nonce"] = nonce
    block_str = json.dumps(block, sort_keys=True).encode()
    hash = hashlib.sha256(block_str).hexdigest()
    while (not isValidHashDifficulty(hash, 4)):
        nonce = nonce + 1
        block["Nonce"] = nonce
        block_str = json.dumps(block, sort_keys=True).encode()
        hash = hashlib.sha256(block_str).hexdigest()
    return hash

# Implementador de Objto ao JSON


def add_block(block):
    if (len(block_chain) == 0):
        hour = datetime.datetime.now().time()
        hour_str = hour.strftime("%H:%M:%S")
        block["Horario "] = hour_str
        block["Hash"] = generate_hash(block)
    else:
        hour = datetime.datetime.now().time()
        hour_str = hour.strftime("%H:%M:%S")
        block["Horario"] = hour_str
        last_block = block_chain[-1]
        block["Last_hash"] = last_block["Hash "]
        block["Hash"] = generate_hash(block)
    block_chain.append(block)


def interface():
    app = ctk.CTk(fg_color='#FFF')
    app.geometry("1000x600")
    app.minsize(width=500, height=300)
    app.resizable(height=False, width=False)
    app._set_appearance_mode('dark')
    app.title("Erion")

    # Configuração dos Frames
    frame1 = ctk.CTkFrame(master=app, fg_color='#FFF', width=900, height=900)
    frame1.place(x=10)
    frame1.pack(pady=60)

    # Configuração da TabView
    tab = ctk.CTkTabview(master=frame1, width=900,
                         height=1000, fg_color="#FFF", segmented_button_selected_color="#02FF58",
                         text_color="#121212", text_color_disabled="#121212",
                         segmented_button_unselected_color="#FFF", segmented_button_selected_hover_color="#02FF58")
    tab.add("Inicio")
    tab.add("Histórico")
    tab.tab("Inicio").grid_columnconfigure(0, weight=2)
    tab.tab("Histórico").grid_columnconfigure(0, weight=2)
    tab.pack()

    # Frame para armazenar a transferencia e o Inicio
    subframe = ctk.CTkFrame(master=tab.tab("Inicio"),
                            width=850, height=500, fg_color="#FFF")
    subframe.place()
    subframe.pack()
    subframe2 = ctk.CTkFrame(master=tab.tab("Histórico"),
                             width=850, height=500, fg_color="#FFF")
    subframe.place()
    subframe2.pack()

    # Frames Incoporados a Pagina de Inicio
    blackframe = ctk.CTkFrame(master=subframe, width=860,
                              height=427, fg_color="#121212", border_width=10, border_color='#121212')
    blackframe.pack()
    blackframe2 = ctk.CTkFrame(master=subframe2, width=860,
                               height=427, fg_color="#121212", border_width=10, border_color='#121212')
    blackframe2.pack()
    whiteframe = ctk.CTkFrame(
        master=blackframe, width=450, height=420, fg_color='#FFF', border_color='#121212', border_width=4)
    whiteframe.place(x=405, y=2)
    whiteframe2 = ctk.CTkFrame(
        master=blackframe2, width=450, height=420, fg_color='#FFF', border_color='#121212', border_width=4)
    whiteframe2.place(x=405, y=2)

    # Imagens utilizadas
    ErionImage = Image.open('ErionLogo.png')
    ErionSpace = ctk.CTkImage(ErionImage, size=(100, 50))
    ErionPosition = ctk.CTkLabel(master=app, image=ErionSpace, text="")
    ErionPosition.place(x=12, y=10)
    UniLogo = Image.open('uniplogo.png')
    UniSpace = ctk.CTkImage(UniLogo, size=(82, 10))
    UniPosition = ctk.CTkLabel(master=app, image=UniSpace, text="")
    UniPosition.place(x=12, y=570)
    Versioninfo = Image.open('version_info.png')
    VersionSpace = ctk.CTkImage(Versioninfo, size=(65, 10))
    VersionPosition = ctk.CTkLabel(master=app, image=VersionSpace, text="")
    VersionPosition.place(x=915, y=570)
    text_1 = Image.open('wx1.png')
    text1_image = ctk.CTkImage(text_1, size=(320, 180))
    text_space = ctk.CTkLabel(master=blackframe, image=text1_image, text="")
    text_space.place(x=50, y=60)
    text_2 = Image.open('wx2.png')
    text2_image = ctk.CTkImage(text_2, size=(255, 50))
    text2_space = ctk.CTkLabel(master=blackframe, image=text2_image, text="")
    text2_space.place(x=55, y=270)
    text_3 = Image.open('wix3.png')
    text3 = ctk.CTkImage(text_3, size=(260, 30))
    text3_space = ctk.CTkLabel(master=whiteframe, image=text3, text="")
    text3_space.place(x=100, y=40)
    historico = Image.open('historicotexto.png')
    historicoconver = ctk.CTkImage(historico, size=(320, 120))
    historicospace = ctk.CTkLabel(
        master=blackframe2, image=historicoconver, text="")
    historicospace.place(x=50, y=100)
    subtext = Image.open('subtext.png')
    subtextconvert = ctk.CTkImage(subtext, size=(250, 50))
    subtextspace = ctk.CTkLabel(
        master=blackframe2, image=subtextconvert, text="")
    subtextspace.place(x=55, y=240)
    historico = Image.open('Histórico.png')
    historicoimage = ctk.CTkImage(historico, size=(120, 20))
    historispace = ctk.CTkLabel(
        master=whiteframe2, image=historicoimage, text="")
    historispace.place(x=170, y=20)

    # Entrada de Dados e Inputs
    nome = ctk.CTkEntry(master=whiteframe, width=350,
                        height=40, placeholder_text="Nome Completo ", placeholder_text_color='grey', fg_color='#FFF', corner_radius=10, text_color="#121212")
    nome.place(x=40, y=90)
    destinatario = ctk.CTkEntry(master=whiteframe, width=350,
                                height=40, placeholder_text="Destinatario ", placeholder_text_color='grey', fg_color='#FFF', corner_radius=10, text_color='#121212')
    destinatario.place(x=40, y=150)
    menu = ctk.CTkOptionMenu(master=whiteframe,
                             values=["BTC", "ETH", "USDT", "BNB", "XRP", "USDC", "SOL"], width=310, height=40, fg_color="#121212", button_color="#02FF58", button_hover_color="#02FF94")
    menu.place(x=40, y=200)
    valor_transfer = ctk.CTkEntry(master=whiteframe, width=350,
                                  height=40, placeholder_text="Valor de Transferência ", placeholder_text_color='grey', fg_color='#FFF', corner_radius=10, text_color='#121212')
    valor_transfer.place(x=40, y=250)
    confirm = ctk.CTkButton(master=whiteframe, text="Enviar",
                            fg_color="#02FF58", text_color="#121212", height=40, hover_color="#02FF94", command=lambda: ObterDados())
    confirm.place(x=155, y=310)
    greenbar = Image.open('green_bar.png')
    greenbarimage = ctk.CTkImage(greenbar, size=(3, 20))
    greenbarimagespace = ctk.CTkLabel(
        master=whiteframe, image=greenbarimage, text="")
    greenbarimagespace.place(x=47, y=95)
    greenbar2 = Image.open('green_bar.png')
    greenbarimage2 = ctk.CTkImage(greenbar2, size=(3, 20))
    greenbarimagespace2 = ctk.CTkLabel(
        master=whiteframe, image=greenbarimage2, text="")
    greenbarimagespace2.place(x=47, y=155)
    greenbar3 = Image.open('green_bar.png')
    greenbarimage3 = ctk.CTkImage(greenbar3, size=(3, 20))
    greenbarimagespace3 = ctk.CTkLabel(
        master=whiteframe, image=greenbarimage3, text="")
    greenbarimagespace3.place(x=47, y=255)
    historico = ctk.CTkTextbox(
        master=whiteframe2, width=410, height=280, fg_color="#FFF", text_color="#121212", scrollbar_button_color="#02FF58", border_color="#121212", border_width=1)
    historico.place(x=20, y=65)
    excelbtn = ctk.CTkButton(master=whiteframe2, text="Ver Tabela no Excel",
                             fg_color="#02FF58", text_color="#121212", height=40, hover_color="#02FF94", command=lambda: ConverterEXCEL())
    excelbtn.place(x=155, y=355)

    # FUNÇÃO DE OBTENÇÃO DE DADOS ATRAVÉS DO BOTÃO

    def ObterDados():
        value1 = ctk.CTkEntry.get(nome)
        value2 = ctk.CTkEntry.get(destinatario)
        value3 = ctk.CTkEntry.get(valor_transfer)
        value4 = ctk.CTkOptionMenu.get(menu)

        if (value3.isdigit() and value1.strip() and value2.strip()):
            try:
                with open(bg_dados, 'r') as file:
                    dados_existentes = json.load(file)
            except FileNotFoundError:
                dados_existentes = []

            update_list = {}
            update_list["Nome"] = value1
            update_list["Destinatario"] = value2
            update_list["Criptomoeda"] = value4
            update_list["Valor"] = value3
            update_list["Hora"] = hora_convertida

            # Adicionar o Hash e o Nonce ao JSON
            update_list["Hash"] = generate_hash(update_list)
            update_list["Nonce"] = update_list["Nonce"]

            hash_valor = update_list["Hash"]
            nonce_valor = update_list["Nonce"]

            dados_existentes.append(update_list)

            with open(bg_dados, 'w') as file:
                json.dump(dados_existentes, file, indent=4)

        # Notificação de Trasição Efetuada
            notificacao = ctk.CTkToplevel(master=blackframe, fg_color="#fff")
            notificacao.title("Notificação")
            notificacao.geometry("300x100")

            label = ctk.CTkLabel(
                master=notificacao, text="Transferência com Sucesso !", fg_color="#FFF", text_color="#121212")
            label.pack(padx=10, pady=10)

            fechar_botao = ctk.CTkButton(
                notificacao, text="Fechar", command=notificacao.destroy, fg_color="#02FF58")
            fechar_botao.pack(pady=5)

            # Fecha automaticamente após 8 segundos
            notificacao.after(8000, notificacao.destroy)

            print("Transição feita com Sucesso!")

            historico.insert('0.2', " Nome : " + value1 +
                             "\n" + " Destinatario : " + value2 + "\n" + " Valor : " + value3 + "\n" + " Criptomoeda : " + value4 + "\n" + " Hora : " + hora_convertida + "\n" + " Hash : " + str(hash_valor) + "\n" + " Nonce : " + str(nonce_valor) + "\n" + "\n")
        else:
            print("Não é um valor válido")
            alertimage = Image.open('alert.png')
            alert = ctk.CTkImage(alertimage, size=(200, 30))
            alertpostion = ctk.CTkLabel(
                master=whiteframe, image=alert, text="")
            alertpostion.place(x=125, y=360)

            alertpostion.after(4000, alertpostion.destroy)

    app.mainloop()


interface()
