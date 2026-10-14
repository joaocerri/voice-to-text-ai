import os
from dotenv import load_dotenv
import whisper as w
from google import genai
load_dotenv()

modelo = w.load_model("base")
transcript = modelo.transcribe("teste.mp3")

client = genai.Client(api_key=os.getenv('API_KEY'))

prompt_text = transcript["text"]

print(f"O prompt enviado por audio foi: {prompt_text}")

try:
    response = client.models.generate_content(
        model='gemini-3.1-flash-lite',
        contents= f'{prompt_text}',
    )

    print(response.text)
except:
    print(f"Erro no processamento do modelo...")

