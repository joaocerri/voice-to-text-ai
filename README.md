# Transcritor e Analisador de Áudio com Whisper e Gemini

Este repositório contém um script em Python que realiza a transcrição de arquivos de áudio localmente utilizando o modelo **Whisper** (da OpenAI) e, em seguida, envia o texto transcrito para a API do **Google Gemini** para processamento inteligente usando o modelo `gemini-3.1-flash-lite`.

## 🚀 Funcionalidades

- **Transcrição Local:** Converte fala em texto a partir de arquivos de áudio (ex: `.mp3`) usando o modelo `base` do Whisper.
- **Integração com IA:** Envia a transcrição gerada para o Google Gemini processar o conteúdo.
- **Segurança de Credenciais:** Utiliza um arquivo `.env` para ocultar sua chave de API com segurança.


## 📋 Pré-requisitos

Antes de começar, você precisará ter instalado em sua máquina:

1. **Python 3.8+**
2. **FFmpeg** (Obrigatório para o funcionamento do Whisper. [Veja como instalar o FFmpeg aqui](https://ffmpeg.org/download.html)).
3. Uma chave de API válida do **Google Gemini** ([Obtenha aqui](https://aistudio.google.com/app/apikey)).

## 🛠️ Instalação

1. Clone este repositório (ou baixe os arquivos para uma pasta local).
2. Abra o terminal na pasta do projeto e instale as bibliotecas necessárias executando o comando abaixo:

```bash
pip install openai-whisper google-genai python-dotenv
```

## ⚙️ Configuração

Para que o script consiga se comunicar com o Google Gemini, você precisa configurar sua chave de API.

1. Na raiz do projeto (mesma pasta do script), crie um arquivo chamado exatamente **`.env`**.
2. Abra o arquivo `.env` e adicione a sua chave no seguinte formato:

```env
API_KEY=sua_chave_de_api_do_google_aqui
```

> **Aviso:** Nunca faça commit do arquivo `.env` no GitHub. Certifique-se de que ele esteja listado no seu arquivo `.gitignore`.

## ▶️ Como Usar

1. Coloque o arquivo de áudio que você deseja transcrever na mesma pasta do script e renomeie-o para `teste.mp3` (ou altere o nome do arquivo diretamente no código Python).
2. Execute o script pelo terminal:

```bash
python nome_do_seu_script.py
```

### O que o script fará:

* Carregará o modelo acústico do Whisper na sua máquina.
* Processará o arquivo `teste.mp3` e imprimirá o texto extraído no console.
* Enviará esse mesmo texto como um prompt para o modelo `gemini-3.1-flash-lite`.
* Imprimirá a resposta gerada pela IA na tela.

## ⚠️ Observações

* **Modelo do Whisper:** O código atual utiliza o modelo `"base"`. Se você tiver um computador com GPU dedicada e quiser maior precisão na transcrição, pode alterar no código para `"small"`, `"medium"` ou `"large"` (lembrando que exigirão mais memória).
* **Disponibilidade da API:** Se a API do Google estiver passando por um pico de acessos, o script exibirá a mensagem `"Servidor ocupado..."`.

