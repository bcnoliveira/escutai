import os
# from google.colab import userdata
from dotenv import load_dotenv
from google import genai
from agents.emotion_detector import emotion_detector
from agents.empathetic_responder import empathetic_responder
from agents.extra_content_provider import video_content_provider
import warnings

from agents.video_validator import video_validator

#Ignorar warnings
warnings.filterwarnings("ignore")

# Configura a API Key do Google Gemini
load_dotenv("environment.txt")
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
# Caso use o Colab, utiliza API Key a partir do userdata
# os.environ["GOOGLE_API_KEY"] = userdata.get('GOOGLE_API_KEY')

# Configura o cliente da SDK do Gemini
client = genai.Client()

def ask_age():
    while True:
        idade_str = input("Por favor, digite sua idade (somente números): ").strip()
        if idade_str.isdigit() and 10 <= int(idade_str) <= 100:
            return int(idade_str)
        else:
            print("⚠️ Entrada inválida. Digite apenas números inteiros de 10 a 100")

print("🧠 EscutAI - Apoio emocional com IA")

# Obter a idade do usuário
user_age = ask_age()
print("Digite uma mensagem de como está se sentindo no momento. Caso deseje sair, pressione enter.")

while True:
    user_message = input("Como se sente? ").strip()

    if not user_message or user_message.lower() in ["sair", ""]:
        print("👋 Até logo! Cuide bem de você.\n")
        break
    else:
        # 1. Classificar emoção
        emotion = emotion_detector(user_message, user_age)
        print(f"\n🧭 Emoção identificada: {emotion}")

        # 2. Gerar resposta empática
        resposta = empathetic_responder(user_message, emotion)
        print(f"🤗 EscutAI: {resposta}")

        # 3. Buscar por conteúdos extras
        print(f"🤗 EscutAI: Para te ajudar, vou tentar buscar um conteúdo extra que pode ser interessante.")
        extra_content = video_content_provider(emotion, user_age)

        # 4. Validar conteudo extra
        is_valid_video = video_validator(extra_content)
        if not is_valid_video:
            # Tenta mais uma vez obter outro video
            is_valid_video = video_content_provider(emotion, user_age)
            validation_response = video_validator(extra_content)
            if not is_valid_video:
                # Fallback para um canal confiável se não conseguir um link válido
                print(f"https://www.youtube.com/@TEDx/search?query={emotion}")
            else:
                print(f"🎥 Aqui está: {extra_content}\n")
        else:
            print(f"🎥 Aqui está: {extra_content}\n")

