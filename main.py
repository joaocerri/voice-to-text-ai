import os
from dotenv import load_dotenv
import whisper as w
from google import genai
import tkinter as tk
from tkinter import filedialog
load_dotenv()

root = tk.Tk()
root.withdraw() 

try:
    arquivo = filedialog.askopenfilename(
        title="Selecione um arquivo MP3",
        filetypes=[("Arquivos MP3", "*.mp3")]
    )
except Exception as erro:
    print(f"Erro no processamento: {erro}")
finally:
    root.destroy()

if not arquivo:
    print("Nenhum arquivo selecionado.")
    raise SystemExit

modelo = w.load_model("base")
transcript = modelo.transcribe(arquivo)

client = genai.Client(api_key=os.getenv('API_KEY'))

prompt_text = transcript["text"]

print(f"O prompt enviado por audio foi: {prompt_text}")

try:
    response = client.models.generate_content(
        model='gemini-3.1-flash-lite',
        contents= f'{prompt_text}',
    )

    print(response.text)
except Exception as erro:
    print(f"Erro no processamento do modelo: {erro}")


