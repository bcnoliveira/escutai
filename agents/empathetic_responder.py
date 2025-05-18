from google.adk.agents import Agent

from agent_caller import call_agent
from contants import GEMINI_MODEL_ID


################################################
# Agente 2: Resposta Empática consoante a emoção
################################################
def empathetic_responder(message: str, emotion: str) -> str:
    if emotion == "alerta":
        # Direciona a pessoa para o CVV imediatamente
        return (
            "Sinto muito por você estar passando por um momento tão difícil. "
            "Saiba que você não está sozinho. O CVV (Centro de Valorização da Vida) oferece apoio emocional gratuito e sigiloso. "
            "Você pode ligar para o número **188**, ou acessar https://cvv.org.br/chat/ para conversar com alguém agora mesmo. "
            "Eles estão disponíveis 24 horas por dia. 💛"
        )
    else:
        # Gera uma resposta empática gerada pela IA
        agent = Agent(
            name="empathetic_responder_agent",
            model=GEMINI_MODEL_ID,
            instruction="""
            Você é um agente empático treinado para oferecer escuta emocional e acolhimento com base na mensagem pela pessoa e na emoção da mensagem.
            Crie uma resposta calorosa e empática, que reconheça o sentimento e acolha a pessoa sem julgamento.
            Não forneça conselhos diretos. Apenas valide o sentimento da pessoa e mostre que ela não está sozinha. 
            """,
            description="Agente que responde de forma empática consoante a emoção"
        )

        message_entry = f"Mensagem:{message}\nEmoção: {emotion}"
        # Executa o agente
        empathetic_answer = call_agent(agent, message_entry)
        return empathetic_answer