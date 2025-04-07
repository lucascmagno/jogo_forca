# 💀 Jogo da Forca - Cyber Edition

## 📌 Sobre o Projeto

Este é um **Jogo da Forca** desenvolvido em **Python** utilizando a biblioteca **PySimpleGUI**. O objetivo é adivinhar a palavra secreta antes que todas as tentativas se esgotem. O visual segue um estilo **futurista cyberpunk**, com elementos em azul neon sobre um fundo escuro, tornando a experiência imersiva e estilizada.

---

## 🎮 Funcionalidades

✅ **Tela Inicial com imagem personalizada** e campo para inserir o nickname  
✅ **Jogo da Forca visual**, com imagem dinâmica da forca conforme os erros  
✅ **Histórico de partidas** salvo em `historico_partidas.txt`, com nickname, resultado e palavra  
✅ **Botão para visualizar histórico** a qualquer momento  
✅ **Palavras aleatórias a cada partida**  
✅ **Tela final com três opções**:  
 🔁 Jogar novamente  
 🏠 Voltar para a tela inicial  
 📜 Ver histórico de partidas  
✅ **Reinício rápido da partida** com o botão "Reiniciar" durante o jogo  
✅ **Sistema de letras erradas e tentativas restantes visível**  
✅ **Interface futurista** com design azul neon + preto

---

## 🛠️ Como Executar o Jogo

### 📌 1. Pré-requisitos

Antes de rodar o jogo, instale o Python e a biblioteca `PySimpleGUI`:

pip install PySimpleGUI
📌 2. Rodando o Jogo
Execute o script no terminal:
python jogo_forca.py

📂 Estrutura Esperada
Organize os arquivos assim:
jogo_forca.py
historico_partidas.txt
img/
├── background.png
├── forca0.png
├── forca1.png
├── forca2.png
├── forca3.png
├── forca4.png
├── forca5.png
├── forca6.png

🎨 Personalização
🎯 Palavras → Edite a lista palavras diretamente no código para adicionar ou remover termos.
🖼️ Imagens → Substitua os arquivos da pasta img/ para alterar o visual da forca ou do fundo.

📜 Histórico de Partidas
Todos os resultados são automaticamente registrados no arquivo historico_partidas.txt, com:

Nickname do jogador

Resultado (vitória ou derrota)

Palavra secreta da rodada

📸 Imagens do Jogo
🔹 Tela Inicial
<img src="https://via.placeholder.com/600x300?text=Tela+Inicial" alt="Tela Inicial">

🔹 Durante o Jogo
<img src="https://via.placeholder.com/600x300?text=Jogo+da+Forca" alt="Jogo da Forca">

🔹 Tela de Fim de Jogo
<img src="https://via.placeholder.com/600x300?text=Resultado+com+op%C3%A7%C3%B5es" alt="Fim do Jogo">

#### 🔧 Tecnologias Utilizadas
🐍 Python
🖼️ PySimpleGUI

🤝 Contribuição
Achou um bug ou quer sugerir melhorias? Sinta-se à vontade para abrir uma issue ou fazer um pull request.

📜 Licença
Este projeto está sob a licença MIT.

🚀 Divirta-se jogando!