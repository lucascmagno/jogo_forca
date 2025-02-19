import PySimpleGUI as sg
import random

# Lista de palavras do jogo
palavras = [
    "python", "computador", "programacao", "janela", "interface",
    "teclado", "monitor", "internet", "sistema", "software",
    "hardware", "inteligencia", "artificial", "neural", "cibernetico"
]

# Histórico de partidas
historico_partidas = []

# Função para iniciar ou reiniciar o jogo
def iniciar_jogo():
    palavra = random.choice(palavras).upper()
    return palavra, ["_"] * len(palavra), [], 6

# Tela inicial
def tela_inicial():
    layout_inicial = [
        [sg.Text("💀 JOGO DA FORCA 💀", font=("Courier New", 24, "bold"), justification="center", expand_x=True)],
        [sg.Button("START", size=(10, 2), font=("Courier New", 16, "bold"), button_color=("#FFFFFF", "#005F8F"))],
        [sg.Button("Sair", size=(10, 2), font=("Courier New", 16, "bold"), button_color=("#FFFFFF", "#8F0000"))]
    ]
    
    janela_inicial = sg.Window("Tela Inicial - Jogo da Forca", layout_inicial, element_justification="center", finalize=True)
    
    while True:
        evento, _ = janela_inicial.read()
        if evento in (sg.WINDOW_CLOSED, "Sair"):
            janela_inicial.close()
            return False
        if evento == "START":
            janela_inicial.close()
            return True

# Iniciar tela inicial
if not tela_inicial():
    exit()

# Iniciar o jogo
palavra_secreta, palavra_display, letras_erradas, tentativas_restantes = iniciar_jogo()

# Tema futurista
sg.theme_background_color("#000814")  
sg.theme_text_color("#00FFFF")  
sg.theme_element_background_color("#001B2E")  
sg.theme_element_text_color("#00FFFF")  
sg.theme_input_background_color("#003C5E")  
sg.theme_input_text_color("#00FFFF")  
sg.theme_button_color(("#FFFFFF", "#005F8F"))  

# Layout do jogo
layout = [
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

        # Validar entrada
        if not letra.isalpha() or len(letra) != 1:
            sg.popup("⚠️ Digite apenas UMA letra válida!", title="Erro", background_color="#000814", text_color="#00FFFF")
            continue

        # Limpar o campo de entrada
        janela["letra"].update("")

        # Verificar se a letra já foi usada
        if letra in palavra_display or letra in letras_erradas:
            sg.popup("⚠️ Você já tentou essa letra!", title="Aviso", background_color="#000814", text_color="#00FFFF")
            continue

        # Se a letra estiver na palavra
        if letra in palavra_secreta:
            for i, char in enumerate(palavra_secreta):
                if char == letra:
                    palavra_display[i] = letra
        else:
            letras_erradas.append(letra)
            tentativas_restantes -= 1

        # Atualizar a interface
        janela["palavra"].update(" ".join(palavra_display))
        janela["erradas"].update(", ".join(letras_erradas))
        janela["tentativas"].update(str(tentativas_restantes))

        # Verificar condições de vitória ou derrota
        if "_" not in palavra_display:
            resultado = f"🎉 Vitória! A palavra era '{palavra_secreta}'"
            historico_partidas.append(resultado)
            break
        if tentativas_restantes == 0:
            resultado = f"💀 Derrota! A palavra era '{palavra_secreta}'"
            historico_partidas.append(resultado)
            break

    if evento == "Reiniciar":
        palavra_secreta, palavra_display, letras_erradas, tentativas_restantes = iniciar_jogo()

        janela["palavra"].update(" ".join(palavra_display))
        janela["erradas"].update("")
        janela["tentativas"].update(str(tentativas_restantes))

janela.close()

# Tela de histórico de partidas
layout_resultados = [
    [sg.Text("📜 Histórico de Partidas 📜", font=("Courier New", 20, "bold"), justification="center", expand_x=True)],
    [sg.Listbox(values=historico_partidas, size=(50, 10), key="historico", font=("Courier New", 14))],
    [sg.Button("Voltar ao Início", font=("Courier New", 14, "bold")), sg.Button("Sair", font=("Courier New", 14, "bold"))]
]

janela_resultados = sg.Window("Resultados", layout_resultados, element_justification="center", finalize=True)

while True:
    evento, _ = janela_resultados.read()
    if evento in (sg.WINDOW_CLOSED, "Sair"):
        break
    if evento == "Voltar ao Início":
        janela_resultados.close()
        if tela_inicial():  # Retorna à tela inicial se o jogador quiser
            palavra_secreta, palavra_display, letras_erradas, tentativas_restantes = iniciar_jogo()
            janela = sg.Window("Jogo da Forca - Cyber Edition", layout, element_justification="center", finalize=True)
        else:
            break

janela_resultados.close()
