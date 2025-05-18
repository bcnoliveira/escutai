from google.adk.agents import Agent
from google.adk.tools import google_search
from datetime import date

from agent_caller import call_agent
from contants import GEMINI_MODEL_ID


######################################
# Agente 4: Validador de Videos Youtube
######################################
def video_validator(link: str) -> bool:
    if not link or "youtube.com/watch" not in link or "youtu.be/" not in link:
        return "NAO"

    agent = Agent(
        name="extra_content_provider_agent",
        model=GEMINI_MODEL_ID,
        instruction=f"""
            Voce deve verificar se um link para um video do youtube está ainda disponível. 
            Responda apenas com SIM ou NAO. Se for um video com link valido responda SIM. Caso contrario, ou caso nao tenha certeza, responda NAO
            """,
        description="Agente validador de links de videos do Youtube",
        tools=[google_search]
    )

    message_entry = f"Link {link}"
    # Executa o agente
    response = call_agent(agent, message_entry)
    return 'SIM' in response.upper()