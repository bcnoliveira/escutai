from google.adk.agents import Agent

from agent_caller import call_agent
from contants import GEMINI_MODEL_ID


##########################################
# Agente 1: Classificador de Emoções
##########################################
def emotion_detector(message: str, user_age: int) -> str:

    agent = Agent(
        name="emotion_detector_agent",
        model=GEMINI_MODEL_ID,
        instruction="""
        Você é um assistente sensível que identifica a emoção de uma mensagem de uma pessoa.
        Primeiro, analise se a mensagem abaixo contém sinais claros de pensamentos relacionados a automutilação ou desejo de acabar com a própria vida.
        Exemplos de sinais incluem: "quero desistir", "não aguento mais", "não quero mais viver", "pensando em suicídio", "não quero continuar".
        - Se a mensagem indicar esses sinais, responda apenas com a palavra: alerta
        - Se não, responda com a principal emoção sentida pela pessoa, usando apenas uma palavra simples, como: tristeza, raiva, ansiedade, alegria, medo, culpa, esperança.
        Lembre-se de ter em consideração a idade da pessoa.
        """,
        description="Agente que detecta emoções com base em uma mensagem"
    )

    message_text = f"Mensagem: {message} Idade: {user_age}"

    emotion = call_agent(agent, message_text)
    return emotion