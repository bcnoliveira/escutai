from google.adk.agents import Agent
from google.adk.tools import google_search
from datetime import date

from agent_caller import call_agent
from contants import GEMINI_MODEL_ID


######################################
# Agente 3: Curador de Conteúdo Extra
######################################
def video_content_provider(emotion: str, user_age: int) -> str:
    if not emotion.strip().lower():
        return ""

    agent = Agent(
        name="extra_content_provider_agent",
        model=GEMINI_MODEL_ID,
        instruction=f"""
            Você é um assistente especializado em pesquisar conteúdos do Youtube. 
            TAREFA:
            1. Use a ferramenta de busca do Google (google_search) para encontrar um vídeo do YouTube atual e relevante sobre como lidar com a emoção: {emotion}
            2. Busque especificamente por vídeos que estejam disponíveis agora no YouTube
            3. Priorize vídeos com muitas visualizações e canais populares (mais chances de estarem ativos)
            4. Escolha conteúdo adequado para uma pessoa de {user_age} anos
            5. Verifique a existência do link antes de retorná-lo (certifique-se que o link começa com "https://www.youtube.com/watch" ou "https://youtu.be/")
            6. Inclua somente um link direto de um vídeo, não de playlists ou canais

            Sugestões de busca:
            - "Como lidar com {emotion} youtube"
            - "Técnicas para {emotion} youtube vídeo"
            - "Meditação para {emotion} youtube"

            MUITO IMPORTANTE: 
            - NÃO retorne links de sites que não sejam o YouTube oficial.
            - Verifique cuidadosamente se o resultado da busca é realmente um link direto para um vídeo do YouTube.
            - Retorne APENAS o link completo e válido do YouTube, nada mais. A sua resposta deve seguir o formato LINK: link do video
            """,
        description="Agente curador de conteudo extra que sugere videos relevantes do Youtube",
        tools=[google_search]
    )

    today = date.today().strftime("%d/%m/%Y")
    message_entry = (f"Encontre um vídeo do YouTube sobre como lidar com a emoção: {emotion}. "
                     f"O vídeo deve ser adequado para alguém de {user_age} anos. Data de hoje: {today}. Retorne apenas o link direto do vídeo.")
    # Executa o agente
    link = call_agent(agent, message_entry)
    return link