import PySimpleGUI as sg
import random
import os

# Lista de palavras do jogo
palavras = [
    "python", "computador", "programacao", "janela", "interface",
    "teclado", "monitor", "internet", "sistema", "software",
    "hardware", "inteligencia", "artificial", "neural", "cibernetico"
]

# Nome do arquivo de histórico
HISTORICO_ARQUIVO = "historico_partidas.txt"
nickname = ""
BACKGROUND_IMG = "background.png"

# Carregar histórico salvo
def carregar_historico():
    if os.path.exists(HISTORICO_ARQUIVO):
        with open(HISTORICO_ARQUIVO, "r", encoding="utf-8") as file:
            return file.read().splitlines()
    return []

# Salvar histórico
def salvar_historico(historico):
    with open(HISTORICO_ARQUIVO, "w", encoding="utf-8") as file:
        file.write("\n".join(historico))

# Função para exibir o histórico de partidas
def ver_historico():
    historico_partidas = carregar_historico()
    
    layout_historico = [
        [sg.Text("📜 Histórico de Partidas 📜", font=("Courier New", 20, "bold"), justification="center")],
        [sg.Listbox(values=historico_partidas, size=(50, 10), key="historico", font=("Courier New", 14))],
        [sg.Button("Voltar", font=("Courier New", 14, "bold"))]
    ]

    janela_historico = sg.Window("Histórico de Partidas", layout_historico, element_justification="center", finalize=True)

    while True:
        evento, _ = janela_historico.read()
        if evento in (sg.WINDOW_CLOSED, "Voltar"):
            break

    janela_historico.close()

# Função para iniciar ou reiniciar o jogo
def iniciar_jogo():
    palavra = random.choice(palavras).upper()
    return palavra, ["_"] * len(palavra), [], 6

# Tela inicial com nickname e background
def tela_inicial():
    global nickname

    layout_inicial = [
        [sg.Image(BACKGROUND_IMG, size=(600, 300))],  # Imagem de fundo
        [sg.Text("Digite seu Nickname:", font=("Courier New", 16, "bold"), text_color="#00FFFF")],
        [sg.Input(key="nickname", size=(20, 1), font=("Courier New", 14))],
        [sg.Button("START", size=(10, 2), font=("Courier New", 16, "bold"), button_color=("#FFFFFF", "#005F8F"))],
        [sg.Button("Ver Histórico", size=(15, 1), font=("Courier New", 14, "bold"), button_color=("#FFFFFF", "#005F8F"))],
        [sg.Button("Sair", size=(10, 2), font=("Courier New", 16, "bold"), button_color=("#FFFFFF", "#8F0000"))]
    ]
    
    janela_inicial = sg.Window("Tela Inicial - Jogo da Forca", layout_inicial, element_justification="center", finalize=True)
    
    while True:
        evento, valores = janela_inicial.read()
        if evento in (sg.WINDOW_CLOSED, "Sair"):
            janela_inicial.close()
            return False
        if evento == "START":
            nickname = valores["nickname"].strip()
            if not nickname:
                sg.popup("⚠️ Por favor, digite um nickname!", title="Aviso")
            else:
                janela_inicial.close()
                return True
        if evento == "Ver Histórico":
            ver_historico()

# Iniciar tela inicial
if not tela_inicial():
    exit()

# Iniciar o jogo
palavra_secreta, palavra_display, letras_erradas, tentativas_restantes = iniciar_jogo()

# Layout do jogo
layout = [
    [sg.Text(f"👤 Jogador: {nickname}", font=("Courier New", 14, "bold"), text_color="#00FFFF")],
    [sg.Text("💀 JOGO DA FORCA 💀", font=("Courier New", 20, "bold"), justification="center", expand_x=True)],
    [sg.Text("Palavra: ", font=("Courier New", 14)), sg.Text(" ".join(palavra_display), key="palavra", font=("Courier New", 14, "bold"))],
    [sg.Text("Tentativas restantes: ", font=("Courier New", 12)), sg.Text(str(tentativas_restantes), key="tentativas", font=("Courier New", 12, "bold"))],
    [sg.Text("Letras erradas: ", font=("Courier New", 12)), sg.Text("", key="erradas", font=("Courier New", 12, "bold"))],
    [sg.Text("Digite uma letra:", font=("Courier New", 12)), sg.Input(size=(5, 1), key="letra"), sg.Button("Tentar", font=("Courier New", 12, "bold"))],
    [sg.Button("Reiniciar", font=("Courier New", 12, "bold")), sg.Button("Sair", font=("Courier New", 12, "bold"))]
]

# Criar a janela do jogo
janela = sg.Window("Jogo da Forca - Cyber Edition", layout, element_justification="center", finalize=True)

while True:
    evento, valores = janela.read()

    if evento == sg.WINDOW_CLOSED or evento == "Sair":
        break

    if evento == "Tentar":
        letra = valores["letra"].strip().upper()

        if not letra.isalpha() or len(letra) != 1:
            sg.popup("⚠️ Digite apenas UMA letra válida!", title="Erro")
            continue

        janela["letra"].update("")

        if letra in palavra_display or letra in letras_erradas:
            sg.popup("⚠️ Você já tentou essa letra!", title="Aviso")
            continue

        if letra in palavra_secreta:
            for i, char in enumerate(palavra_secreta):
                if char == letra:
                    palavra_display[i] = letra
        else:
            letras_erradas.append(letra)
            tentativas_restantes -= 1

        janela["palavra"].update(" ".join(palavra_display))
        janela["erradas"].update(", ".join(letras_erradas))
        janela["tentativas"].update(str(tentativas_restantes))

        if "_" not in palavra_display:
            resultado = f"{nickname} 🎉 Vitória! A palavra era '{palavra_secreta}'"
            historico_partidas = carregar_historico()
            historico_partidas.append(resultado)
            salvar_historico(historico_partidas)
            sg.popup(resultado)
            break
        if tentativas_restantes == 0:
            resultado = f"{nickname} 💀 Derrota! A palavra era '{palavra_secreta}'"
            historico_partidas = carregar_historico()
            historico_partidas.append(resultado)
            salvar_historico(historico_partidas)
            sg.popup(resultado)
            break

    if evento == "Reiniciar":
        palavra_secreta, palavra_display, letras_erradas, tentativas_restantes = iniciar_jogo()
        janela["palavra"].update(" ".join(palavra_display))
        janela["erradas"].update("")
        janela["tentativas"].update(str(tentativas_restantes))

janela.close()
