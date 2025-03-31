# Código traduzido para Português (mantendo nomes de classes/métodos e sintaxe Python)
from agno.agent import Agent, Toolkit
from agno.tools.duckduckgo import DuckDuckGoTools
import os

class ReportAnalyzerAgent(Toolkit):
    """
    ReportAnalyzerAgent é um toolkit que analisa laudos para classificar em Patologia, Radiologia, Genética ou Laboratório
    para então chamar o agente apropriado.
    """
    def __init__(self, model): # Aceita o modelo, se necessário
        super().__init__(name="report_analyzer_agent") # Nome técnico da toolkit mantido em inglês
        self.agent = Agent(
            name="Agente Analisador de Laudo", # Nome traduzido
            model=model, # Usa o modelo passado
            tools=[DuckDuckGoTools()],
            instructions="Você é um analisador de laudos que analisa relatórios para classificar em Patologia, Radiologia, Genética ou Laboratório", # Instruções traduzidas
            tool_call_limit=3,
            show_tool_calls=True
        )

    def query(self, question): # 'query' mantido como nome do método
        response = self.agent.run(question)
        return response

class PathologyAgent(Toolkit):
    """
    PathologyAgent é um toolkit que analisa laudos de patologia / biópsia para explicar os
    achados para médicos solicitantes e escalar para humano em caso de incerteza.
    """
    def __init__(self, model): # Aceita 'model' como argumento
        super().__init__(name="pathology_agent") # Nome técnico da toolkit mantido em inglês
        self.agent = Agent(
            name="Agente de Patologia", # Nome traduzido
            model=model, # Usa o modelo passado
            tools=[DuckDuckGoTools()],
            instructions="Você é um Especialista em Patologia auxiliando médicos solicitantes. Responda claramente ou escale para humano se incerto.", # Instruções traduzidas
            tool_call_limit=3,
            show_tool_calls=True
        )

    def query(self, question): # 'query' mantido como nome do método
        response = self.agent.run(question)
        return response

class GeneticAgent(Toolkit):
    """
    GeneticAgent é um toolkit que analisa laudos genéticos para explicar os
    achados para médicos solicitantes e escalar para humano em caso de incerteza.
    """
    def __init__(self, model): # Aceita 'model' como argumento
        super().__init__(name="genetic_agent") # Nome técnico da toolkit mantido em inglês
        self.agent = Agent(
            name="Agente de Genética", # Nome traduzido
            model=model, # Usa o modelo passado
            tools=[DuckDuckGoTools()],
            instructions="Você é um Especialista em Genética auxiliando médicos solicitantes. Responda claramente ou escale para humano se incerto.", # Instruções traduzidas
            tool_call_limit=3,
            show_tool_calls=True
        )

    def query(self, question): # 'query' mantido como nome do método
        response = self.agent.run(question)
        return response

class RadiologyAgent(Toolkit):
    """
    RadiologyAgent é um toolkit que analisa laudos de radiologia para explicar os
    achados para médicos solicitantes e escalar para humano em caso de incerteza.
    """
    def __init__(self, model): # Aceita 'model' como argumento
        super().__init__(name="radiology_agent") # Nome técnico da toolkit mantido em inglês
        self.agent = Agent(
            name="Agente de Radiologia", # Nome traduzido
            model=model, # Usa o modelo passado
            tools=[DuckDuckGoTools()],
            instructions="Você é um Especialista em Radiologia auxiliando médicos solicitantes. Responda claramente ou escale para humano se incerto.", # Instruções traduzidas
            tool_call_limit=3,
            show_tool_calls=True
        )

    def query(self, question): # 'query' mantido como nome do método
        response = self.agent.run(question)
        return response

class LaboratoryAgent(Toolkit):
    """
    LaboratoryAgent é um toolkit que analisa laudos laboratoriais para explicar os
    achados para médicos solicitantes e escalar para humano em caso de incerteza.
    """
    def __init__(self, model): # Aceita 'model' como argumento
        super().__init__(name="laboratory_agent") # Nome técnico da toolkit mantido em inglês
        self.agent = Agent(
            name="Agente de Resultados Laboratoriais", # Nome traduzido
            model=model, # Usa o modelo passado
            tools=[DuckDuckGoTools()],
            instructions="Você é um Especialista Laboratorial auxiliando médicos solicitantes. Responda claramente ou escale para humano se incerto.", # Instruções traduzidas
            tool_call_limit=3,
            show_tool_calls=True
        )

    def query(self, question): # 'query' mantido como nome do método
        response = self.agent.run(question)
        return response